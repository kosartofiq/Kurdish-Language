from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


class Job(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='jobs',
        related_query_name='job',
        verbose_name=_('Creator Id')
    )
    # Fields
    name = models.CharField(
        _('Job Name'),
        max_length=100,
        help_text=_("Name of the job.")
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        help_text=_("Description about the job.")
    )
    timestamp = models.DateTimeField(
        _('Created Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('job')
        verbose_name_plural = _('jobs')

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
        return reverse('job-detail', kwargs={'pk': self.pk})

    # OTHER METHODS


class JobHistory(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    editor = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='job_histories',
        related_query_name='job_history',
        verbose_name=_('Editor Id')
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='job_histories',
        related_query_name='job_history',
        verbose_name=_('Job Id')
    )
    # Fields
    name = models.CharField(
        _('Job Name'),
        max_length=100,
        help_text=_("Name of the job.")
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        help_text=_("Description about the job.")
    )
    timestamp = models.DateTimeField(
        _('Edited Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('job history')
        verbose_name_plural = _('job histories')

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
        # return reverse('job-detail', kwargs={'pk': self.pk})

    # OTHER METHODS
