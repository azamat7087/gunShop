from django.contrib import admin
from .models import *
# Register your models here.

class GunsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'body', 'image', 'date_pub']
    list_filter = ['body', 'image', 'date_pub']
    list_editable = ['body', 'image',]
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Guns, GunsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class InfoOfUserAdmin(admin.ModelAdmin):
    list_display = ['name',  'body', 'date_of_birth', 'sex']
    list_filter = ['body', 'image', 'date_of_birth']

admin.site.register(InfoOfUser, InfoOfUserAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'gun_slug', 'date_of_add']
    list_filter = ['name', 'user', 'gun_slug', 'date_of_add']

admin.site.register(Cart, CartAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'gun_main', 'date_of_add', 'body', 'user_img']
    list_filter = ['user', 'gun_main', 'date_of_add', 'body', 'user_img']

admin.site.register(Comment, CommentAdmin)