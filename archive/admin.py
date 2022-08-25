from django.contrib import admin

from archive.models import Storage, Metadata
# Register your models here.

admin.site.register(Storage)
admin.site.register(Metadata)