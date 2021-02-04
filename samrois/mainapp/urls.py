# DjangoImports
from django.urls import path
# End DjangoImports

# InternalImports
from . import views
# End InternalImports

# UrlPatterns
urlpatterns = [
    path('', views.redirect_to_index),
    path('order_add', views.order_add, name='order_create'),

    # RU
    path('ru/', views.index, name='ru_index'),
    path('ru/tours/', views.tour_list, name='ru_tour_list'),
    path('ru/tours/<int:tour_id>/', views.tour_detail, name='ru_tour_detail'),
    path('ru/thank-you/', views.thank_you, name='ru_thank_you'),
    # End RU

    # EN
    path('en/', views.index, name='en_index'),
    path('en/tours/', views.tour_list, name='en_tour_list'),
    path('en/tours/<int:tour_id>/', views.tour_detail, name='en_tour_detail'),
    path('en/thank-you/', views.thank_you, name='en_thank_you'),
    # End EN

    # KO
    path('ko/', views.index, name='ko_index'),
    path('ko/tours/', views.tour_list, name='ko_tour_list'),
    path('ko/tours/<int:tour_id>/', views.tour_detail, name='ko_tour_detail'),
    path('ko/thank-you/', views.thank_you, name='ko_thank_you'),
    # End KO

]
# End UrlPatterns

