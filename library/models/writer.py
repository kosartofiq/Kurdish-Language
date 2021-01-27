from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


class Writer(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='writers',
        related_query_name='writer',
        verbose_name=_('Creator Id')
    )
    # Fields
    name = models.CharField(
        _('Writer Name'),
        max_length=100,
        help_text=_("Name of the writer.")
    )
    born_date = models.DateField(
        _('Writer Born'),
        blank=True,
        null=True,
        help_text=_('Born date of writer.')
    )
    died_date = models.DateField(
        _('Writer Died '),
        blank=True,
        null=True,
        help_text=_('Died date of writer.')
    )
    profile = models.TextField(
        _('Profile'),
        blank=True,
        help_text=_("Profile about the writer.")
    )
    image = models.ImageField(
        _('Image'),
        default='default_writer.jpg',
        upload_to='writer_pics',
        help_text=_('Picture of the writer.')
    )
    timestamp = models.DateTimeField(
        _('Created Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('writer')
        verbose_name_plural = _('writers')

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
        return reverse('writer-detail', kwargs={'pk': self.pk})

    # OTHER METHODS


class WriterHistory(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    editor = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='writer_histories',
        related_query_name='writer_history',
        verbose_name=_('Editor Id')
    )
    writer = models.ForeignKey(
        Writer,
        on_delete=models.CASCADE,
        related_name='writer_histories',
        related_query_name='writer_history',
        verbose_name=_('Writer Id')
    )
    # Fields
    name = models.CharField(
        _('Writer Name'),
        max_length=100,
        help_text=_("Name of the writer.")
    )
    born_date = models.DateField(
        _('Writer Born'),
        blank=True,
        null=True,
        help_text=_('Born date of writer.')
    )
    died_date = models.DateField(
        _('Writer Died '),
        blank=True,
        null=True,
        help_text=_('Died date of writer.')
    )
    profile = models.TextField(
        _('Profile'),
        blank=True,
        help_text=_("Profile about the writer.")
    )
    image = models.ImageField(
        _('image'),
        upload_to='writer_pics',
        help_text=_('Picture of the writer.')
    )
    timestamp = models.DateTimeField(
        _('Edited Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('writer history')
        verbose_name_plural = _('writer histories')

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
        # return reverse('writer-detail', kwargs={'pk': self.pk})

    # OTHER METHODS
