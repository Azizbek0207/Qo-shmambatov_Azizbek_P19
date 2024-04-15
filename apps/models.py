from multiprocessing.reduction import AbstractReducer

from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, EmailField, IntegerField, ImageField, DateField, ForeignKey, CASCADE, \
    TextChoices, URLField, FloatField, DateTimeField, ManyToManyField


# Create your models here.


# class Blog(Model):
#     name = CharField(max_length=255)
#     description = CharField(max_length=255)
#     photo = ImageField()
#     tag = ManyToManyField('Tag')
#     created_at = DateTimeField(auto_now_add=True)

class Blog(Model):
    title = CharField(max_length=255)
    description = CharField(max_length=255)
    photo = ImageField()
    category = ForeignKey('apps.Category', CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    user = ForeignKey('apps.User', CASCADE)


class Category(Model):
    title = CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)


class User(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)

    