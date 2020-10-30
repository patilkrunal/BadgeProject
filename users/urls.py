from django.urls import path
from django.conf.urls import url

from users.views import Profile

app_name = 'users'

urlpatterns = [
    path('profile/<str:username>/', Profile, name='profile'),
]
