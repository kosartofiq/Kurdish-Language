from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


class Language(models.Model):
    # CHOICES

    # DATABASE FIELDS
    creator = models.ForeignKey( 
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='languages',
        related_query_name='language',
        verbose_name=_('Creator Id'))
    #
    name = models.CharField(_('Langauge Name'), max_length=100, unique=True)
    native_name = models.CharField(
        _('Native Language Name')
        max_length=100,
        unique=True,
        help_text=_("Name of language and written in native of it's Language"))
    iso_639_1 = models.CharField(
        _('ISO 639-1')
        max_length=2,
        unique=True,
        help_text=_('for more info: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes'))
    iso_639_2 = models.CharField(
        _('ISO 639-2')
        max_length=3,
        unique=True,
        help_text=_('for more info: https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes'))
    description = models.TextField(_('Description'), blank=True)
    timestamp = models.DateTimeField(_('Created Date'), auto_now_add=True)
    
    # MANAGERS
    # languages = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('language')
        verbose_name_plural = _('languages')

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
        return reverse('language-detail', kwargs={'pk': self.id})

    # OTHER METHODS

