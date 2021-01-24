from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


class Location(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='locations',
        related_query_name='location',
        verbose_name=_('Creator Id')
    )
    # Fields
    name = models.CharField(
        _('Location Name'),
        max_length=100,
        help_text=_("Name of the location.")
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        help_text=_("Description about the location.")
    )
    timestamp = models.DateTimeField(
        _('Created Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('location')
        verbose_name_plural = _('locations')

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
        return reverse('location-detail', kwargs={'pk': self.pk})

    # OTHER METHODS


class LocationHistory(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    editor = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='location_histories',
        related_query_name='location_history',
        verbose_name=_('Editor Id')
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='location_histories',
        related_query_name='location_history',
        verbose_name=_('Location Id')
    )
    # Fields
    name = models.CharField(
        _('Location Name'),
        max_length=100,
        help_text=_("Name of the location.")
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        help_text=_("Description about the location.")
    )
    timestamp = models.DateTimeField(
        _('Edited Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('location history')
        verbose_name_plural = _('location histories')

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
        # return reverse('location-detail', kwargs={'pk': self.pk})

    # OTHER METHODS
