from django.contrib import admin

from .models import Color

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    model=Color
    list_display = ('staff','color')