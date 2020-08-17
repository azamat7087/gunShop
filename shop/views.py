from django.shortcuts import render, redirect,reverse
from django.views import View
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404
# Create your views here.

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
        gun_cart = Cart.objects.filter(user__iexact=login)
        user_obj = InfoOfUser.objects.get(login__iexact=login)
        return render(request, 'shop/cart.html', context={'guns': gun_cart,'cash': user_obj.cash})

class GunDelete(LoginRequiredMixin, View):
    def get(self, request, login, gun):

        gun = Cart.objects.get(gun_slug__iexact=gun, user__iexact=login)
        return render(request, 'shop/delete_from_cart.html', context={'gun': gun, 'login':login})

    def post(self, request, login, gun):
        gun = Cart.objects.get(gun_slug__iexact=gun, user__iexact=login)
        gun.delete()
        return redirect('main')

