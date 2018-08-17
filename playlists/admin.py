"""Django admin module"""
from django.contrib import admin
from .models import Track, Artist, Release


# do this instead -
# https://docs.djangoproject.com/en/2.1/topics/db/models/#meta-options
@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    """"Special class to layout rules for Track in admin"""
    list_display = ('number', 'name', 'length', 'release')
    ordering = ('number',)


admin.site.register(Artist)
admin.site.register(Release)
