from django.db import models

from movieschallenge.apps.core.models import TimestampedModel


class Person(TimestampedModel):
    """Person"""
    
    first_name = models.CharField(db_index=True, max_length=255, unique=True)
    last_name = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    aliases = models.CharField(db_index=True, max_length=255, unique=True)
    movies_as_actor = models.ForeignKey('apps.Movies', related_name='actors', on_delete=models.CASCADE)
    movies_as_director = models.ForeignKey(
        'apps.Movies', related_name='directors', on_delete=models.CASCADE)
    movies_as_producer = models.ForeignKey(
        'apps.Movies', related_name='producers', on_delete=models.CASCADE)

    def __str__(self):

        return self.email


    def get_full_name(self):

        return f'{self.first_name} {self.last_name}'

    def get_aliases(self):

        return self.aliases
