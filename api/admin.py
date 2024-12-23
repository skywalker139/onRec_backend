from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .resource import PodcastResource, GuestResource, BlogResource
from .models import *
from django import forms
# Register your models here.

class ReportAdmin(ImportExportModelAdmin):
     resource_class = PodcastResource      
admin.site.register(Podcast, ReportAdmin)

class ReportAdmin(ImportExportModelAdmin):
     resource_class = GuestResource      
admin.site.register(Guest, ReportAdmin)

class BlogForm(forms.ModelForm):
    content = forms.JSONField(
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        help_text='Enter JSON data in the format: [{"heading": "Heading 1", "paragraph": "Paragraph 1"}, ...]'
    )

    class Meta:
        model = Blog
        fields = '__all__'

class BlogAdmin(ImportExportModelAdmin):
    resource_class = BlogResource
    form = BlogForm

admin.site.register(Blog, BlogAdmin)
