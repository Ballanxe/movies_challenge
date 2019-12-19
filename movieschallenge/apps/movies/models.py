from django.db import models

from movieschallenge.apps.core.models import TimestampedModel
from movieschallenge.apps.persons.models import Person


class Movie(TimestampedModel):

    title = models.CharField('Title',db_index=True, max_length=255)
    release_year = models.DateField('Release year')
    casting = models.ManyToManyField(Person, related_name='casting')
    directors = models.ManyToManyField(Person, related_name='directors')
    producers = models.ManyToManyField(Person, related_name='producers')

    def __str__(self):
        return self.title.capitalize()
