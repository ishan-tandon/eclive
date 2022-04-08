from django.urls import path
from input_portal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.AboutView, name='about'),
    path('about/', views.AboutView, name='about'),
    path('draggable/', views.DraggableView.as_view(), name='drag'),
    path('embed/', views.EmbedView.as_view(), name='embed'),
    path('estimatorstandings/', views.LeaderView, name='estimatorstandings'),
    path('teamstandings/', views.TeamLeaderView, name='teamstandings'),
    path('results/<str:racecode>/', views.ResultsView, name='results'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
