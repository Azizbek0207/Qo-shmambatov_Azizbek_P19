from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.models import ContactsPage


# Register your models here.
@admin.register(ContactsPage)
class PersonAdmin(ImportExportModelAdmin):
    pass
