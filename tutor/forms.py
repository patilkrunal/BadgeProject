from django import forms
from django.contrib.auth.models import User

from .models import Profile


class tutorUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']


class profileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['bio','profile_pic']
