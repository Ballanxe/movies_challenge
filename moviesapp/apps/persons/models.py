from django.db import models
from django.contrib.auth import get_user_model

from moviesapp.apps.core.models import TimestampedModel
from moviesapp.apps.movies.models import Movie

User = get_user_model()


class Person(TimestampedModel):
    """Person"""

    aliases = models.CharField(db_index=True, max_length=255, unique=True)
    movies_as_actor = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='fromactors')
    movies_as_director = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='persons+')
    movies_as_producer = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='persons+')
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def __str__(self):

        return self.email

    def get_full_name(self):

        return f'{self.first_name} {self.last_name}'

    def get_aliases(self):

        return self.aliases
