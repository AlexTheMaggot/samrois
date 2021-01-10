# DjangoImports
from django.urls import path
# End DjangoImports

# InternalImports
from . import views
# End InteralImports

# UrlPatterns
urlpatterns = [
    path('', views.redirect_to_index),

    # RU
    path('ru/', views.index, name='ru_index'),
    # End RU

    # EN
    path('en/', views.index, name='en_index'),
    # End EN

    # KO
    path('ko/', views.index, name='ko_index'),
    # End KO

]
# End UrlPatterns
