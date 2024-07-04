# movies/urls.py

from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieDetail, MoviesList, CategoryList



urlpatterns = [
    path('movies/<str:code>/', MovieDetail.as_view(), name='movie-detail'),
    path('movies_list/', MoviesList.as_view(), name='movies_list'),
    path('category_list/', CategoryList.as_view(), name='category_list'),
]