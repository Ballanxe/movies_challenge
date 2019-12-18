from django.db import models

from movieschallenge.apps.core.models import TimestampedModel


class Movie(TimestampedModel):

    title = models.CharField('Title',db_index=True, max_length=255)
    release_year = models.DateField('Release year')
    casting = models.ManyToManyField('app.Persons', related_name='casting')
    directors = models.ManyToManyField('app.Persons', related_name='directors')
    producers = models.ManyToManyField('app.Persons', related_name='producers')

	def __str__(self):
		return self.title.capitalize()
