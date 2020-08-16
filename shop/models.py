from django.db import models


# Create your models here.

class Guns(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=30, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    category = models.ForeignKey('Category',null=True, on_delete=models.CASCADE,default="",)
    image = models.ImageField(upload_to='static/images/guns/', blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_pub']

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=30, blank=True, unique=True)

    def __str__(self):
        return self.name

class InfoOfUser(models.Model):
    name = models.CharField(max_length=150,db_index=True)
    login = models.CharField(max_length=150, unique=True,default="")
    sex = models.CharField(max_length=10, db_index=True)
    image = models.ImageField(upload_to='static/images/users/', blank=True)
    body = models.TextField(max_length=200,db_index=True,default="")
    date_of_birth = models.DateTimeField()

    def __str__(self):
        return self.name

