from django.db.models import Model, CharField, EmailField, IntegerField, ImageField, DateField


# Create your models here.


class ContactsPage(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    location = CharField(max_length=255)
    photo = ImageField()
    email = EmailField()
    phone = IntegerField()


