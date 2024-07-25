from django.urls import path
from .views import (MoviesList,
                    CategoryList,
                    TreylerList,
                    EpisodeList,
                    UsersList
                    )


urlpatterns = [
    path('movies_list/', MoviesList.as_view(), name='movies_list'),
    path('users/', UsersList.as_view(), name='users'),
    path('category_list/', CategoryList.as_view(), name='category_list'),
    path('treyler/', TreylerList.as_view(), name='treyler_list'),
    path('episode/', EpisodeList.as_view(), name='episode_list'),
]
