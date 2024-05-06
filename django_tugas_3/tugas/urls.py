from django.urls import path
from . import views

urlpatterns = [
    path('tugas/', views.tugas, name='tugas'),
    path('tugasdb/', views.tugasdb, name='tugasdb'),
]