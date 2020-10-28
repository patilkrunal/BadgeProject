from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include(('home.urls', 'home'), namespace='home')),

    path('', include('courses.urls',namespace='courses')),
    path('', include('memberships.urls',namespace='memberships')),
    path('', include('tutor.urls',namespace='tutor')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
