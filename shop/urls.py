from django.urls import path
from .views import *

urlpatterns = [

    path('', main, name='main'),
    path('news/', News.as_view(), name='news'),
    path('users/<str:login>/', UserDetail.as_view(), name='user_detail_url'),
    path('<str:name>/', gun_list, name='gun_list_url'),
    path('<str:name>/<str:slug>/', GunDetail.as_view(), name='gun_detail_url'),
    path('<str:name>/<str:slug>/<str:login>/add_comment/', AddComment.as_view(), name='add_comment_url'),
    path('<str:name>/<str:slug>/buy/', GunBuy.as_view(), name='gun_buy_url'),
    path('users/<str:login>/cart/<str:gun>/', GunInCart.as_view(), name='gun_cart_url'),
    path('users/<str:login>/basket/', UserCart.as_view(), name='user_cart_url'),
    path('users/<str:login>/basket/<str:gun>/delete/', GunDelete.as_view(), name='gun_delete_url'),
    path('users/<str:login>/basket/buy/<str:total>', UserBuy.as_view(), name='user_buy_url'),
    path('users/<str:login>/purchase/', PurchaseUser.as_view(), name='purchase_user_url'),
    path('users/<str:login>/create/', CreateInfo.as_view(), name='create_info_url'),
    path('users/<str:login>/update/', UpdateInfo.as_view(), name='update_info_url'),


]