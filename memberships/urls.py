from django.urls import path
from .views import StudentsListView

app_name = 'memberships'

urlpatterns = [
    path('addmembers/', StudentsListView.add_members, name='add_members'),
    # path('redirect', CourseDetailRedirect.as_view(), name='memberships_redirect'),
]
