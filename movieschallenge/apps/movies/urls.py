from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import (
	ArticleViewSet,
	CommentsListCreateAPIView,
	CommentsDestroyAPIView,
	ArticlesFavoriteAPIView,
	TagListAPIView,
	ArticlesFeedAPIView
)


router = DefaultRouter(trailing_slash=False)
router.register(r'articles', ArticleViewSet)

urlpatterns = [

	url(r'^articles/feed/?$', ArticlesFeedAPIView.as_view()),
	url(r'^articles/(?P<article_slug>[-\w]+)/favorite/?$',
	    ArticlesFavoriteAPIView.as_view()),
	url(r'^articles/(?P<article_slug>[-\w]+)/comments/?$',
	    CommentsListCreateAPIView.as_view()),
	url(r'^articles/(?P<article_slug>[-\w]+)/comments/(?P<comment_pk>[\d]+)/?$',
	    CommentsDestroyAPIView.as_view()),
	url(r'^tags/?$', TagListAPIView.as_view()),
	url(r'^', include(router.urls)),

]
