from django.shortcuts import render, redirect,reverse
from django.views import View
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from matplotlib import pyplot
import numpy as np
from PIL import Image
import cv2
import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FuncFormatter,MaxNLocator


def gun_list(request, name):
    category = Category.objects.get(slug__iexact=name)
    gun_list = Guns.objects.filter(category=category.id)

    paginator = Paginator(gun_list, 3)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ""

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ""


    return render(request, 'shop/guns_list.html', context={'gun_list': gun_list,
                                                           'name': name,
                                                           'page_object': page,
                                                           'is_paginated': is_paginated,
                                                           'prev_url': prev_url,
                                                           'next_url': next_url
                                                           })

def main(request):
    return render(request, 'shop/main.html')

class GunDetail(View):
    def get(self, request, slug, name):
        gun = Guns.objects.get(slug__iexact=slug)

        is_already_in_cart = True

        try:
            in_cart = Cart.objects.get(user=request.user, gun_slug=slug)
        except:
            in_cart = False

        if in_cart:
            is_already_in_cart = False

        return render(request, 'shop/gun_detail.html', context={"gun": gun, 'name': name, 'already': is_already_in_cart})


class UserDetail(LoginRequiredMixin, View):
    def get(self, request, login):
        if str(login) == str(request.user):
            users = InfoOfUser.objects.all()
            list = []
            for user in users:
                list.append(str(user.login))

            if login not in list:
                return redirect('create_info_url',login=login, permanent=True)

            else:
                user1 = InfoOfUser.objects.get(login=login)
                return render(request, 'shop/user_detail.html', context={'user': user1})
        else:
            return redirect('main', permanent=True)


class GunBuy(LoginRequiredMixin, View):
    def get(self, request, slug, name):
        gun = Guns.objects.get(slug__iexact=slug)
        user = request.user

        return render(request, 'shop/buy.html', context={'gun': gun,'user': user,'name': name})


class GunInCart(LoginRequiredMixin, View):
    def get(self, request, login, gun):
        gun = Guns.objects.get(name__contains=gun)
        product = Cart.objects.create(name = gun.name, user=request.user, gun_slug=gun.slug, image=gun.image)

        return render(request, 'shop/gun_detail_1.html', context={'gun': gun})


class UserCart(LoginRequiredMixin, View):

    def get(self, request, login):
        if str(login) == str(request.user):
            pass
        else:
            return redirect('main', permanent=True)

        gun_all = Guns.objects.all()
        gun_cart = Cart.objects.filter(user__iexact=login)
        user_obj = InfoOfUser.objects.get(login__iexact=login)
        total = 0
        for gun in gun_cart:
            for gun1 in gun_all:
                if gun1.slug == gun.gun_slug:
                    total += gun1.price

        return render(request, 'shop/cart.html', context={'guns': gun_cart,'cash': user_obj.cash, 'gun_all': gun_all,'total': total })


class GunDelete(LoginRequiredMixin, View):
    def get(self, request, login, gun):
        if str(login) == str(request.user):
            pass
        else:
            return redirect('main', permanent=True)

        gun = Cart.objects.get(gun_slug__iexact=gun, user__iexact=login)
        return render(request, 'shop/delete_from_cart.html', context={'gun': gun, 'login':login})

    def post(self, request, login, gun):
        gun = Cart.objects.get(gun_slug__iexact=gun, user__iexact=login)
        gun.delete()

        return redirect('main')


class UserBuy(LoginRequiredMixin, View):
    def get(self, request, login, total):
        if str(login) == str(request.user):
            pass
        else:
            return redirect('main', permanent=True)
        gun_all = Guns.objects.all()
        guns = Cart.objects.filter(user__iexact=login)
        user = InfoOfUser.objects.get(login__iexact=login)
        cash = user.cash
        cash_after = float(cash) - float(total)

        return render(request, 'shop/user_buy.html', context={'user': user, 'cash': cash, 'cash_after': cash_after, 'total': total, 'guns': guns, 'gun_all': gun_all})

    def post(self, request, login, total):
        guns = Cart.objects.filter(user__iexact=login)
        for gun in guns:
            purchase = Purchase.objects.create(login=login, gun_slug=gun.gun_slug, image=gun.image )

        guns.delete()

        guns_1 = Purchase.objects.filter(login__iexact=login)
        paginator = Paginator(guns_1, 3)

        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ""

        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ""

        cash = InfoOfUser.objects.get(login__iexact=login).cash
        cash_after = float(cash) - float(total)

        user = InfoOfUser.objects.get(login__iexact=login)

        if request.method == "POST":
            user.cash = cash_after
            user.save()

        return render(request, 'shop/purchase.html', context={'guns': guns_1, 'login': login, 'page_object': page,
                                                                'is_paginated': False,
                                                                'prev_url': prev_url,
                                                                'next_url': next_url})

class PurchaseUser(View):
    def get(self, request, login):
        if str(login) == str(request.user):
            pass
        else:
            return redirect('main', permanent=True)

        purchase = Purchase.objects.filter(login__iexact=login)
        paginator = Paginator(purchase, 3)

        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ""

        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ""

        return render(request, 'shop/purchase.html', context={'guns': purchase,
                                                              'login': login,
                                                                'page_object': page,
                                                                'is_paginated': is_paginated,
                                                                'prev_url': prev_url,
                                                                'next_url': next_url}
                                                                 )

class CreateInfo(View):

    def post(self, request, login):
        bound_form = InfoOfUserForm(request.POST, request.FILES)

        if bound_form.is_valid():
            bound_form.save()
            info = InfoOfUser.objects.get(name__iexact=login)
            info.login = login
            info.save()
            return redirect('user_detail_url', login=login)

        return render(request, 'shop/create_info_of_user.html', context={'form': bound_form})

    def get(self, request, login):
        form = InfoOfUserForm()
        return render(request, 'shop/create_info_of_user.html', context={'form': form,'login': login})

class UpdateInfo(View):
    def get(self, request, login):
        obj = InfoOfUser.objects.get(login__iexact=login)
        bound_form = InfoOfUserForm(instance=obj)

        return render(request, 'shop/update_info.html', context={'form': bound_form, 'login': login})

    def post(self, request, login):
        obj = InfoOfUser.objects.get(login__iexact=login)
        bound_form = InfoOfUserForm(request.POST,request.FILES, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect('user_detail_url', login=login)
        return render(request, 'shop/update_info.html', context={'form': bound_form})

class News(View):
    def get(self, request):
        news = Purchase.objects.all()
        users = InfoOfUser.objects.all()
        diogramm(self, users)
        return render(request, 'shop/news.html', context={'news': news, 'users': users})


def imageOnImage(largeImg , smallImg,x_offset, y_offset ):
    y1, y2 = y_offset, y_offset + smallImg.shape[0]
    x1, x2 = x_offset, x_offset + smallImg.shape[1]

    alpha_s =1
    print(alpha_s)
    alpha_l = 0

    for c in range(0, 3):
        largeImg[y1:y2, x1:x2, c] = (alpha_s * smallImg[:, :, c] + alpha_l * largeImg[y1:y2, x1:x2, c])

def diogramm(self, users_info):
    users = InfoOfUser.objects.all()
    users_in_purchase = Purchase.objects.all()
    users_list = []
    purchace_list = []
    count_list = dict()
    count = 0

    for user in users:
        users_list.append(user.login)

    for user in users_in_purchase:
        purchace_list.append(user.login)


    for user in users_list:
        for p_user in purchace_list:
            if p_user == user:
                count += 1

        count_list[user] = count
        count = 0

    users = []
    count = []

    for k, v in count_list.items():
        users.append(k)
        count.append(int(v))


    fig, ax = plt.subplots()

    ax.barh(users, count, align='edge',
            color='green', ecolor='black', )

    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.set_xlabel('Weapons purchased')

    plt.title("Top customers")
    plt.savefig('shop\\static\\images\\news\\Empty_pylpot.png')

    images = []
    for user in users_info:
        images.append(user.image)

    height = 700
    width = 800
    # create layer or void image
    layer = np.zeros((height, width, 3))
    background = layer[:]
    cv2.imwrite('shop\\static\\images\\news\\res.png', background)
    # call saved diagram
    background = cv2.imread('shop\\static\\images\\news\\res.png')
    img = cv2.imread('shop\\static\\images\\news\\Empty_pylpot.png')
    reImg = cv2.resize(img, (background.shape[1], background.shape[0]))
    imageOnImage(background, reImg, 0, 0)

    for i in range(1, len(users)+1):
        si = cv2.resize(cv2.imread('shop/{}'.format(images[-i])),(65, 45))
        imageOnImage(background, si, 14, (110+(i-1)*85))
    cv2.imwrite('shop\\static\\images\\news\\final.png', background)
