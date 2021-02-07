from django import forms
from .import models


class CreateCourse(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['title','branch_of_study','description']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Please add a title. Max: 65 characters'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe your course. Max: 400 characters'})
        }


class CreateBranch(forms.ModelForm):
    class Meta:
        model = models.Branch_of_study
        fields = ['branch_of_study']

        widgets = {
            'branch_of_study': forms.TextInput(attrs={'placeholder': 'Add new branch of study. Max: 150 characters'})
        }
