# DjangoImports
from django.urls import path
# End DjangoImports

# InternalImports
from . import views
# End InternalImports

# UrlPatterns
urlpatterns = [
    path('', views.redirect_to_index),

    # RU
    path('ru/', views.index, name='ru_index'),
    path('ru/tours/', views.tour_list, name='ru_tour_list'),
    path('ru/tours/<int:tour_id>/', views.tour_detail, name='ru_tour_detail'),
    path('ru/thank-you/', views.thank_you, name='ru_thank_you'),
    path('ru/order_add/', views.order_add, name='ru_order_create'),
    # End RU

    # EN
    path('en/', views.index, name='en_index'),
    path('en/tours/', views.tour_list, name='en_tour_list'),
    path('en/tours/<int:tour_id>/', views.tour_detail, name='en_tour_detail'),
    path('en/thank-you/', views.thank_you, name='en_thank_you'),
    path('en/order_add/', views.order_add, name='en_order_create'),
    # End EN

    # KO
    path('ko/', views.index, name='ko_index'),
    path('ko/tours/', views.tour_list, name='ko_tour_list'),
    path('ko/tours/<int:tour_id>/', views.tour_detail, name='ko_tour_detail'),
    path('ko/thank-you/', views.thank_you, name='ko_thank_you'),
    path('ko/order_add/', views.order_add, name='ko_order_create'),
    # End KO

    # UZ
    path('uz/', views.index, name='uz_index'),
    path('uz/tours/', views.tour_list, name='uz_tour_list'),
    path('uz/tours/<int:tour_id>/', views.tour_detail, name='uz_tour_detail'),
    path('uz/thank-you/', views.thank_you, name='uz_thank_you'),
    path('uz/order_add/', views.order_add, name='uz_order_create'),
    # End UZ

]
# End UrlPatterns

