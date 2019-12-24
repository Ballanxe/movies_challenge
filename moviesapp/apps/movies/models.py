from django.db import models

from moviesapp.apps.core.models import TimestampedModel


class Movie(TimestampedModel):

    title = models.CharField('Title', db_index=True, max_length=255)
    release_year = models.DateField('Release year')
    casting = models.ManyToManyField('persons.Person', related_name='movies+')
    directors = models.ManyToManyField('persons.Person', related_name='movies+')
    producers = models.ManyToManyField('persons.Person', related_name='movies+')
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return self.title.capitalize()
