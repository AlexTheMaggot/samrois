from django.contrib import admin
from .models import Slide, Tour, Order


class SlideConfig(admin.ModelAdmin):
    list_display = ('pk', 'image')


admin.site.register(Slide, SlideConfig)


class TourConfig(admin.ModelAdmin):
    pass


admin.site.register(Tour, TourConfig)


class OrderConfig(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'tour')


admin.site.register(Order, OrderConfig)
