# movies/urls.py

from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieDetail, get_episodes_by_series_code


urlpatterns = [
    path('movies/<str:code>/', MovieDetail.as_view(), name='movie-detail'),
    path('series/<str:code>/episodes/', get_episodes_by_series_code, name='get_episodes_by_series_code'),
]
