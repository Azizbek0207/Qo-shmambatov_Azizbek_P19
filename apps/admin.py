from django.contrib import admin

from apps.models import Member, User


# Register your models he
#


@admin.register(Member)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass