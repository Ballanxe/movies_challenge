from django.db import models
from django.contrib.auth import get_user_model

from movieschallenge.apps.core.models import TimestampedModel
from movieschallenge.apps.movies.models import Movie

User = get_user_model()

class Person(TimestampedModel, User):
    """Person"""

    aliases = models.CharField(db_index=True, max_length=255, unique=True)
    movies_as_actor = models.ForeignKey(Movie, related_name='actors', on_delete=models.CASCADE)
    movies_as_director = models.ForeignKey(
        Movie, related_name='directors', on_delete=models.CASCADE)
    movies_as_producer = models.ForeignKey(
        Movie, related_name='producers', on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def __str__(self):

        return self.email


    def get_full_name(self):

        return f'{self.first_name} {self.last_name}'

    def get_aliases(self):

        return self.aliases
