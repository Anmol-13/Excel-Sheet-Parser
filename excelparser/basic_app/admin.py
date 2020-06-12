from django.contrib import admin
from .models import Address
from import_export.admin import ImportExportModelAdmin
# admin.site.register(Address)

@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    pass
