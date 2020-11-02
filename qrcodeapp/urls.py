from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import badge_generator_view

urlpatterns = [
    # path('search/myqrcode/', badge_generator_view, name='badge_generator_view'),
]
