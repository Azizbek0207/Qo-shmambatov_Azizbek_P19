from django.contrib import admin

from apps.models import Blog, Category, User


# Register your models he
#
#
#
#
# re.

@admin.register(Blog)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass