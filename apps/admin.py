from django.contrib import admin

from apps.models import CreativeTeam, Director


# Register your models here.
@admin.register(CreativeTeam)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Director)
class PersonAdmin(admin.ModelAdmin):
    pass
