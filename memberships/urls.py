from django.urls import path
from .views import StudentsListView


app_name = 'memberships'

urlpatterns = [
    path('memberships/', StudentsListView.as_view(), name='select_membership')
]
