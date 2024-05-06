from django.contrib import admin

from apps.models import Contact, Position, Member, Job, PositionTag, Blog, Category, Email


# Register your models he
#


@admin.register(PositionTag)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Member)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Job)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    pass
