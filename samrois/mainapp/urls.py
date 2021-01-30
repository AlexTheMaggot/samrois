# DjangoImports
from django.urls import path
# End DjangoImports

# InternalImports
from . import views
# End InteralImports

# UrlPatterns
urlpatterns = [
    path('', views.redirect_to_index),
    path('order_add', views.order_add, name='order_create'),

    # RU
    path('ru/', views.index, name='ru_index'),
    path('ru/tours/', views.tour_list, name='ru_tour_list'),
    path('ru/tours/<int:tour_id>/', views.tour_detail, name='ru_tour_detail'),
    # End RU

    # EN
    path('en/', views.index, name='en_index'),
    path('en/tours/', views.tour_list, name='en_tour_list'),
    path('en/tours/<int:tour_id>/', views.tour_detail, name='en_tour_detail'),
    # End EN

    # KO
    path('ko/', views.index, name='ko_index'),
    path('ko/tours/', views.tour_list, name='ko_tour_list'),
    path('ko/tours/<int:tour_id>/', views.tour_detail, name='ko_tour_detail'),
    # End KO

]
# End UrlPatterns

