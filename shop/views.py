from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
# Create your views here.

def gun_list(request, name):
    category = Category.objects.get(slug__iexact=name)
    gun_list = Guns.objects.filter(category=category.id)
    return render(request, 'shop/guns_list.html', context={'gun_list': gun_list, 'name': name})

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