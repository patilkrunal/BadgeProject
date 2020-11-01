from django.urls import path
from .views import StudentsListView, SearchResultsView, submit

app_name = 'memberships'

urlpatterns = [
    path('addmembers/', StudentsListView.add_members, name='add_members'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search/submit/', submit, name='search_submit')
]
