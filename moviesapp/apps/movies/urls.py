from django.urls import re_path, path

from .views import (
    MovieUpdateDestroyAPIView,
    MovieCreateAPIView,
    MovieRetrieveAPIView,
    MovieListAPIView
)

urlpatterns = [
    re_path(r'movies/(?P<movie_id>[\d]+)/', MovieUpdateDestroyAPIView.as_view(), name='create'),
    path(r'movies/', MovieListAPIView.as_view(), name='owner-list'),
    re_path(r'movie/(?P<movie_id>[\d]+)/', MovieRetrieveAPIView.as_view(), name='retrieve'),
    path(r'movie/', MovieCreateAPIView.as_view(), name='admin-list'),
]
