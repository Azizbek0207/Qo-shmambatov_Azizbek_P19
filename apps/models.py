from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, ImageField, FloatField
from django.utils.translation import gettext_lazy as _




class Member(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    profession = CharField(max_length=255)
    image = ImageField(upload_to='rasm')
    address = CharField(max_length=255)
    rating = FloatField()


class User(AbstractUser):
    photo = ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
