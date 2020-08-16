from django.shortcuts import render
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

        return render(request, 'shop/gun_detail.html', context={"gun": gun, 'name': name})

class UserDetail(View):
    def get(self, request, login):
        user = InfoOfUser.objects.get(login=login)

        return render(request, 'shop/user_detail.html', context={'user': user})

