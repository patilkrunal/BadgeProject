from django.urls import path

from .views import Profile

app_name = 'tutor'

urlpatterns = [
    path('profile/', Profile, name='profile'),
]
