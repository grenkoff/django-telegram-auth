from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from a_api.views import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        TemplateView.as_view(
            template_name='index.html', content_type='text/html',
        ),
    ),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    re_path('^social/', include('social_django.urls', namespace='social')),
    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf')),
]
