from django import forms
from .import models


class CreateCourse(forms.ModelForm):
  class Meta:
    model = models.Course
    
    fields = ['creator','slug','title','branch_of_study','description','starting_date','ending_date']
