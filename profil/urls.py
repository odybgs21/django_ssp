from django.urls import path
from . import views

urlpatterns = [
    path('omah/', views.home, name='home'),
    path('cerita/', views.cerita, name='cerit'),
    path('berita/', views.berita, name='berita'),
]