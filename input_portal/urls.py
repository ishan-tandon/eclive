from django.urls import path
from input_portal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.AboutView.as_view(), name='about'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('draggable/', views.DraggableView.as_view(), name='drag'),
    path('estimatorstandings/', views.LeaderView, name='estimatorstandings'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
