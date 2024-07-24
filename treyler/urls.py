from django.urls import path

from .views import AddTreylerView




urlpatterns = [
    path('trey/', AddTreylerView.as_view(), name='add')
]
