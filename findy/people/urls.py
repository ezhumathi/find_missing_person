from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_people, name='search_people'),
    path('face-search/', views.face_search, name='face_search'),
]