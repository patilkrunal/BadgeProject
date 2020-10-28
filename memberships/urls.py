from django.urls import path
from .views import MembershipSelectView
                  

app_name = 'memberships'

urlpatterns = [
    path('memberships/', MembershipSelectView.as_view(), name='select_membership')
]
