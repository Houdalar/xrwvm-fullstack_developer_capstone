from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
import os

urlpatterns = [
    path('login/', TemplateView.as_view(template_name="index.html")),
    path('register/', TemplateView.as_view(template_name="index.html")),
    path('dealers/', TemplateView.as_view(template_name="index.html")),

    path('manifest.json', serve, {
        'document_root': os.path.join(settings.BASE_DIR, 'frontend/build'),
        'path': 'manifest.json'
    }),
    path('admin/', admin.site.urls),
    path('logo192.png', serve, {
        'document_root': os.path.join(settings.BASE_DIR, 'frontend/build'),
        'path': 'logo192.png'
    }),
    path('logo512.png', serve, {
        'document_root': os.path.join(settings.BASE_DIR, 'frontend/build'),
        'path': 'logo512.png'
    }),

    path('djangoapp/', include('djangoapp.urls')),
    path('', TemplateView.as_view(template_name="Home.html")),
    path('about/', TemplateView.as_view(template_name="About.html")),
    path('contact/', TemplateView.as_view(template_name="Contact.html")),
    path('dealer/<int:dealer_id>', TemplateView.as_view(template_name="index.html")),
    path('postreview/<int:dealer_id>/', TemplateView.as_view(template_name="index.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
