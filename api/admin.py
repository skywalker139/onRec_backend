from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .resource import PodcastResource, GuestResource
from .models import *
# Register your models here.

class ReportAdmin(ImportExportModelAdmin):
     resource_class = PodcastResource      
admin.site.register(Podcast, ReportAdmin)

class ReportAdmin(ImportExportModelAdmin):
     resource_class = GuestResource      
admin.site.register(Guest, ReportAdmin)