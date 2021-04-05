from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

# we import separately because when import them together make circular import
# problem
# from .  import Genre, Job, Location, Publisher, Writer
from .book import Book

PAGE_TYPES = (
    (1, _('Page')),
    (2, _('Page')),
)


class Page(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='pages',
        related_query_name='page',
        verbose_name=_('Creator Id')
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name='pages',
        related_query_name='page',
        verbose_name=_('Book Id')
    )

    # Fields
    number = models.CharField(
        _('Page Number'),
        max_length=100,
        help_text=_("Number of the page(1,2,... | a,b,...).")
    )
    page_type = models.SmallIntegerField(
        _('Page Type'),
        choices=PAGE_TYPES,
        default=1,
        help_text=_("Type of page.")
    )
    preview_page = models.BigIntegerField(
        _('Preview Page'),
        default=0,
        help_text=_("Number of page that this page will come after it.")
    )
    is_blank = models.BooleanField(
        _('Is blank?'),
        default=False,
        help_text=_('For determine if the page is blank.')
    )
    is_finished = models.BooleanField(
        _('Is Finished?'),
        default=False,
        help_text=_('For determine if the page is finished to rewrite all text.')
    )
    image = models.ImageField(
        _('Image'),
        default='default_page.jpg',
        upload_to='page_pics',
        help_text=_('Picture of the page.')
    )
    timestamp = models.DateTimeField(
        _('Created Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')

    # TO STRING METHOD
    def __str__(self):
        return self.number

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


class PageHistory(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    editor = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='page_histories',
        related_query_name='page_history',
        verbose_name=_('Editor Id')
    )
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        related_name='page_histories',
        related_query_name='page_history',
        verbose_name=_('Page Id'))

    # Fields
    number = models.CharField(
        _('Page Number'),
        max_length=100,
        help_text=_("Number of the page(1,2,... | a,b,...).")
    )
    page_type = models.SmallIntegerField(
        _('Page Type'),
        choices=PAGE_TYPES,
        default=1,
        help_text=_("Type of page.")
    )
    preview_page = models.BigIntegerField(
        _('Preview Page'),
        default=0,
        help_text=_("Number of page this page will come after.")
    )
    is_blank = models.BooleanField(
        _('Is blank?'),
        default=False,
        help_text=_('For determine if the page is blank.')
    )
    is_finished = models.BooleanField(
        _('Is Finished?'),
        default=False,
        help_text=_('For determine if the page is finished to rewrite all text.')
    )
    image = models.ImageField(
        _('Image'),
        default='default_page.jpg',
        upload_to='page_pics',
        help_text=_('Picture of the page.')
    )
    timestamp = models.DateTimeField(
        _('Created Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('page history ')
        verbose_name_plural = _('page histories')

    # TO STRING METHOD
    def __str__(self):
        return self.number

    # SAVE METHOD
    def save(self, *args, **kwargs):
        # do_something()
        super().save(*args, **kwargs)
        # do_something_else()

    # ABSOLUTE URL METHOD
    # def get_absolute_url(self):
    # return reverse('book-detail', kwargs={'pk': self.pk})

    # OTHER METHODS

