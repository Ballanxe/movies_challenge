from rest_framework import viewsets
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
)
from .serializers import PersonSerializer
from .renderers import PersonJSONRenderer
from .models import Person


class PersonViewSet(viewsets.ModelViewSet):

	serializer_class = PersonSerializer
	permission_classes = (AllowAny,)
	queryset = Person.objects.all()
	renderer_classes = (PersonJSONRenderer,)