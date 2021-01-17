from django.contrib import admin
from .models import Slide, Tour


class SlideConfig(admin.ModelAdmin):
    list_display = ('pk', 'image')


admin.site.register(Slide, SlideConfig)


class TourConfig(admin.ModelAdmin):
    pass


admin.site.register(Tour, TourConfig)
