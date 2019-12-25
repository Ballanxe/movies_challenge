from django.db import models

from moviesapp.apps.core.models import TimestampedModel
from moviesapp.apps.movies.models import Movie


class Person(TimestampedModel):
    """Person"""

    first_name = models.CharField(db_index=True, max_length=255)
    last_name = models.CharField(db_index=True, max_length=255)
    aliases = models.CharField(db_index=True, max_length=255)
    movies_as_actor = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='fromactors')
    movies_as_director = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='persons+')
    movies_as_producer = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='persons+')


    def __str__(self):

        return self.email

    def get_full_name(self):

        return f'{self.first_name} {self.last_name}'

    def get_aliases(self):

        return self.aliases
