from django import forms
from .import models


class AddMembers(forms.ModelForm):
  class Meta:
    model = models.StudentMembership
    
    fields = ['student_name','email_id','course']
