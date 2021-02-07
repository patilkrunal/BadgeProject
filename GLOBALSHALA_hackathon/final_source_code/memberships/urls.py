from django.urls import path
from memberships.views import StudentsListView, SearchResultsView, badge_generator_view

app_name = 'memberships'

urlpatterns = [
    path('addmembers/', StudentsListView.add_members, name='add_members'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search/<int:member_id>', badge_generator_view, name='badge_generator_view')
]