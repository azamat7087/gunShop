from django.urls import path
from .views import *

urlpatterns = [

    path('', main, name='main'),
    path('users/<str:login>/', UserDetail.as_view(), name='user_detail_url'),
    path('<str:name>/', gun_list, name='gun_list_url'),
    path('<str:name>/<str:slug>/', GunDetail.as_view(), name='gun_detail_url'),

]