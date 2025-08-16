from django.contrib import admin

# Register your models here.
from .models import URL,Custom_url



@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ('original_url','created_at')


@admin.register(Custom_url)
class Custom_urlAdmin(admin.ModelAdmin):
    list_display = ('original_url','created')