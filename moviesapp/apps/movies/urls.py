from django.urls import re_path, path

from .views import (
    MovieUpdateCreateDestroyAPIView,
    MovieRetrieveListAPIView,
)

urlpatterns = [
    re_path(r'movies/(?P<movie_id>[\d]+)/', MovieUpdateDestroyAPIView.as_view(), name='create'),
    path(r'movies/', ReviewOwnerListAPIView.as_view(), name='owner-list'),
    re_path(r'reviews/(?P<review_id>[\d]+)/', ReviewRetrieveAPIView.as_view(), name='retrieve'),
    path(r'admin/reviews/', ReviewAdminAPIView.as_view(), name='admin-list'),
]
