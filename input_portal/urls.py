from django.urls import path
from input_portal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.AboutView.as_view(), name='about'),
    path('about/', views.AboutView.as_view(), name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
