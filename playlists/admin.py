"""Django admin module"""
from django.contrib import admin
from .models import Track, Artist, Release


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    """"Special class to layout rules for Track in admin"""
    list_display = ('number', 'name', 'length', 'release')
    ordering = ('number',)


admin.site.register(Artist)
admin.site.register(Release)
