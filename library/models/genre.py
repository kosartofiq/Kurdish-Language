from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


class Genre(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='genres',
        related_query_name='genre',
        verbose_name=_('Creator Id')
    )
    # Fields
    name = models.CharField(
        _('Genre Name'),
        max_length=100,
        help_text=_("Name of the genre.")
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        help_text=_("Description about the genre.")
    )
    timestamp = models.DateTimeField(
        _('Created Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('genre')
        verbose_name_plural = _('genres')

    # TO STRING METHOD
    def __str__(self):
        return self.name

    # SAVE METHOD
    def save(self, *args, **kwargs):
        # do_something()
        super().save(*args, **kwargs)
        # do_something_else()

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('genre-detail', kwargs={'pk': self.pk})

    # OTHER METHODS


class GenreHistory(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    editor = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='genre-histories',
        related_query_name='genre-history',
        verbose_name=_('Editor Id')
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name='genre_histories',
        related_query_name='genre_history',
        verbose_name=_('Genre Id')
    )
    # Fields
    name = models.CharField(
        _('Genre Name'),
        max_length=100,
        help_text=_("Name of the genre.")
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        help_text=_("Description about the genre.")
    )
    timestamp = models.DateTimeField(
        _('Edited Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('genre history')
        verbose_name_plural = _('genre histories')

    # TO STRING METHOD
    def __str__(self):
        return self.name

    # SAVE METHOD
    def save(self, *args, **kwargs):
        # do_something()
        super().save(*args, **kwargs)
        # do_something_else()

    # ABSOLUTE URL METHOD
    # def get_absolute_url(self):
        # return reverse('genre-detail', kwargs={'pk': self.pk})

    # OTHER METHODS
