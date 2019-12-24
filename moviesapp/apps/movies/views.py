from rest_framework import generics, status, mixins
from rest_framework.exceptions import NotFound
from rest_framework.permissions import (IsAuthenticated, AllowAny)
from rest_framework.response import Response

from .serializers import MovieSerializer
from .models import Movie
from .renderers import MovieJSONRenderer


class MovieUpdateDestroyAPIView(mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                generics.GenericAPIView):
    lookup_url_kwarg = 'movie_id'
    permission_classes = (IsAuthenticated,)
    renderer_classes = (MovieJSONRenderer,)
    serializer_class = MovieSerializer


class MovieCreateAPIView(generics.CreateAPIView):

    queryset = Movie.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = MovieSerializer
    renderer_classes = (MovieJSONRenderer,)

    def create(self, request):

        data = request.data.get('movie', {})
        context = {}
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
            context['ip_address'] = ip
        else:
            ip = request.META.get('REMOTE_ADDR')
            context['ip_address'] = ip

        serializer = self.serializer_class(data=data, context=context)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieRetrieveAPIView(generics.RetrieveAPIView):

    lookup_url_kwarg = 'movie_id'
    permission_classes = (AllowAny,)
    renderer_classes = (MovieJSONRenderer,)
    serializer_class = MovieSerializer


class MovieListAPIView(mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       generics.GenericAPIView):

    queryset = Movie.objects.all()
    permission_classes = (AllowAny,)
    renderer_classes = (MovieJSONRenderer,)
    serializer_class = MovieSerializer
