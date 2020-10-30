from django.urls import path

from .views import (HomeView,
                    AboutView,
                    ContactView,
                    CourseListView,
                    CourseDetailView
                    )

app_name = 'courses'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<slug>/', CourseDetailView.as_view(), name='course_detail')
]



