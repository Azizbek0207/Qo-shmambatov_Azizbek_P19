from django.contrib import admin

from apps.models import Member

# Register your models he
#


@admin.register(Member)
class ProductAdmin(admin.ModelAdmin):
    pass
