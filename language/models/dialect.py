from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from .language import Language


class Dialect(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='dialects',
        related_query_name='dialect',
        verbose_name=_('Creator Id')
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.PROTECT,
        related_name='dialects',
        related_query_name='dialect',
        verbose_name=_('Language Id')
    )
    super_dialect = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='sub_dialects',
        related_query_name='sub_dialect',
        blank=True,
        null=True,
        verbose_name=_('Super Dialect Id')
    )
    # Fields
    name = models.CharField(
        _('Dialect Name'),
        max_length=100,
        help_text=_("Name of the dialect.")
    )
    native_name = models.CharField(
        _('Native Dialect Name'),
        max_length=100,
        help_text=_("Name of the dialect and written in native of it's language.")
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        help_text=_("Description about the dialect.")
    )
    timestamp = models.DateTimeField(
        _('Created Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('dialect')
        verbose_name_plural = _('dialects')
        #  constraint to for each language only unique dialect name
        constraints = [
            models.UniqueConstraint(
                fields=['language', 'name'],
                name=_('Unique dialect to a language')
            )
        ]

    # TO STRING METHOD
    def __str__(self):
        return self.name

    # SAVE METHOD
    def save(self, *args, **kwargs):
        # do_something()
        super().save(*args, **kwargs)
        # do_something_else()

    # ABSOLUTE URL METHOD
    def get_absolute_url(self, pk1):
        return reverse('dialect-detail', kwargs={'pk1': pk1, 'pk2': self.pk})

    # OTHER METHODS



