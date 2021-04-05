from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

# we import separately because when import them together make circular import
# problem
# from .  import Genre, Job, Location, Publisher, Writer
from .page import Page


class Paragraph(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='paragraphs',
        related_query_name='paragraph',
        verbose_name=_('Creator Id')
    )
    page = models.ForeignKey(
        Page,
        on_delete=models.PROTECT,
        related_name='paragraphs',
        related_query_name='paragraph',
        verbose_name=_('Location Id')
    )

    # Fields
    text = models.CharField(
        _('Paragraph Text'),
        max_length=100,
        help_text=_("Text of paragraph")
    )
    preview_paragraph = models.BigIntegerField(
        _('Preview Paragraph'),
        default=0,
        help_text=_("Number of paragraph in page that this paragraph will come after it.")
    )
    trail_paragraph = models.BigIntegerField(
        _('Trail Paragraph'),
        default=0,
        help_text=_("Number of paragraph in preview page that this paragraph will complete the text,"
                    "  for example on paragraph divided in 2 pages.")
    )
    timestamp = models.DateTimeField(
        _('Created Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('paragraph')
        verbose_name_plural = _('paragraphs')

    # TO STRING METHOD
    def __str__(self):
        return self.text

    # SAVE METHOD
    def save(self, *args, **kwargs):
        # do_something()
        super().save(*args, **kwargs)
        # do_something_else()

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        pass
        # return reverse('book-detail', kwargs={'pk': self.pk})

    # OTHER METHODS


class ParagraphHistory(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    editor = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='paragraph_histories',
        related_query_name='paragraph_history',
        verbose_name=_('Editor Id')
    )
    paragraph = models.ForeignKey(
        Paragraph,
        on_delete=models.CASCADE,
        related_name='paragraph_histories',
        related_query_name='paragraph_history',
        verbose_name=_('Paragraph Id'))

    # Fields
    text = models.CharField(
        _('Paragraph Text'),
        max_length=100,
        help_text=_("Text of paragraph")
    )
    preview_paragraph = models.BigIntegerField(
        _('Preview Paragraph'),
        default=0,
        help_text=_("Number of paragraph in page that this paragraph will come after it.")
    )
    trail_paragraph = models.BigIntegerField(
        _('Trail Paragraph'),
        default=0,
        help_text=_("Number of paragraph in preview page that this paragraph will complete the text,"
                    "  for example on paragraph divided in 2 pages.")
    )
    timestamp = models.DateTimeField(
        _('Created Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('paragraph history ')
        verbose_name_plural = _('paragraph histories')

    # TO STRING METHOD
    def __str__(self):
        return self.text

    # SAVE METHOD
    def save(self, *args, **kwargs):
        # do_something()
        super().save(*args, **kwargs)
        # do_something_else()

    # ABSOLUTE URL METHOD
    # def get_absolute_url(self):
    # return reverse('book-detail', kwargs={'pk': self.pk})

    # OTHER METHODS

