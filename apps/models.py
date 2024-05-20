from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, ImageField, ForeignKey, CASCADE, ManyToManyField, IntegerField, \
    FloatField, TextField, DateTimeField, EmailField
from django.utils.translation import gettext_lazy as _


# Importing the Category model from the same module


# class Position(Model):
#     name = CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
#
# class Contact(Model):
#     first_name = CharField(max_length=255)
#     last_name = CharField(max_length=255)
#     image = ImageField(upload_to='rasm')
#     email = EmailField()
#     position = ForeignKey("apps.Position", CASCADE)
#
#
# #########################################################################
#
#
# class PositionTag(Model):
#     name = CharField(max_length=255)
#
#     def __str__(self):
#         return self.name


class Member(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    profession = CharField(max_length=255)
    image = ImageField(upload_to='rasm')
    address = CharField(max_length=255)
    rating = FloatField()

#
# class Job(Model):
#     name = CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
#
# class UploadImage(Model):
#     caption = CharField(max_length=200)
#     image = ImageField(upload_to='rasm')
#
#     def __str__(self):
#         return self.caption
#
#
# class Blog(Model):
#     title = CharField(max_length=255)
#     image = ImageField()
#     description = TextField()
#     author = ForeignKey('auth.User', on_delete=CASCADE)
#     posted_at = DateTimeField(auto_now_add=True)
#     category = ForeignKey('apps.Category', CASCADE)
#
#
# class Category(Model):
#     name = CharField(max_length=255)
#
#     class Meta:
#         verbose_name = _('category')
#
#
# class Email(Model):
#     email = EmailField()
#     password = CharField(max_length=6)
