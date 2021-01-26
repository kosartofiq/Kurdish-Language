from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


class Publisher(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='publishers',
        related_query_name='publisher',
        verbose_name=_('Creator Id')
    )
    # Fields
    name = models.CharField(
        _('Publisher Name'),
        max_length=100,
        help_text=_("Name of the publisher.")
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        help_text=_("Description about the publisher.")
    )
    logo = models.ImageField(
        _('logo'),
        default='default_publisher.jpg',
        upload_to='publisher_logos',
        help_text=_('Logo of the publisher.')
    )
    timestamp = models.DateTimeField(
        _('Created Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('publisher')
        verbose_name_plural = _('publishers')

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
        return reverse('publisher-detail', kwargs={'pk': self.pk})

    # OTHER METHODS


class PublisherHistory(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    editor = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='publisher_histories',
        related_query_name='publisher_history',
        verbose_name=_('Editor Id')
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name='publisher_histories',
        related_query_name='publisher_history',
        verbose_name=_('Publisher Id')
    )
    # Fields
    name = models.CharField(
        _('Publisher Name'),
        max_length=100,
        help_text=_("Name of the publisher.")
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        help_text=_("Description about the publisher.")
    )
    logo = models.ImageField(
        _('logo'),
        upload_to='publisher_logos',
        help_text=_('Logo of the publisher.')
    )
    timestamp = models.DateTimeField(
        _('Edited Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('publisher history')
        verbose_name_plural = _('publisher histories')

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
        # return reverse('publisher-detail', kwargs={'pk': self.pk})

    # OTHER METHODS
