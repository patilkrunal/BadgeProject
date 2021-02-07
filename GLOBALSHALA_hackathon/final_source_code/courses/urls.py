from django.urls import path

from .views import CourseListView, CourseDetailView

app_name = 'courses'

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/create/', CourseListView.course_create, name='course_create'),
    path('courses/create_branch/', CourseDetailView.branch_create, name='branch_create'),
    path('courses/<slug>/', CourseDetailView.as_view(), name='course_detail')
]
