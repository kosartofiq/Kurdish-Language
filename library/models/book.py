from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

# we import separately because when import them together make circular import problem
# from . import Genre, Job, Location, Publisher, Writer
from .genre import Genre
from .job import Job
from .location import Location
from .publisher import Publisher
from .writer import Writer
from language.models.language import Language


class Book(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='books',
        related_query_name='book',
        verbose_name=_('Creator Id')
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name='books',
        related_query_name='book',
        verbose_name=_('Location Id')
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.PROTECT,
        related_name='books',
        related_query_name='book',
        verbose_name=_('Publisher Id')
    )
    genres = models.ManyToManyField(
        Genre,
        related_name='books',
        related_query_name='book',
        verbose_name=_('Genre Id')
    )
    languages = models.ManyToManyField(
        Language,
        related_name='books',
        related_query_name='book',
        verbose_name=_('Language Id')
    )
    writers = models.ManyToManyField(
        Writer,
        related_name='books',
        related_query_name='book',
        through='BookWriter',
        verbose_name=_('Writer Id')
    )
    # Fields
    name = models.CharField(
        _('Book Name'),
        max_length=100,
        help_text=_("Name of the book.")
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        help_text=_("Description about the book.")
    )
    year = models.DateField(
        _('Publish Year'),
        blank=True,
        null=True,
        help_text=_('Year of the publishing the book.')
    )
    edition_number = models.IntegerField(
        _('Edition Number'),
        blank=True,
        null=True,
        help_text=_('Number of the book edition.')
    )
    volume = models.IntegerField(
        _('Volume Number'),
        blank=True,
        null=True,
        help_text=_('Number of the book volume.')
    )
    part = models.IntegerField(
        _('Part Number'),
        blank=True,
        null=True,
        help_text=_('Number of the book part.')
    )
    page_quantity = models.IntegerField(
        _('Page Quantity'),
        help_text=_('Quantity of the book pages.')
    )
    is_copyright = models.BooleanField(
        _('Is copyright?'),
        default=False,
        help_text=_('For determine if the book is copyrighted ')
    )
    image = models.ImageField(
        _('Image'),
        default='default_book.jpg',
        upload_to='book_pics',
        help_text=_('Picture of the book.')
    )
    timestamp = models.DateTimeField(
        _('Created Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')

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
        return reverse('book-detail', kwargs={'pk': self.pk})

    # OTHER METHODS


# many to many table through
class BookWriter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.PROTECT)
    writer = models.ForeignKey(Writer, on_delete=models.PROTECT)


class BookHistory(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    editor = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='book_histories',
        related_query_name='book_history',
        verbose_name=_('Editor Id')
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='book_histories',
        related_query_name='book_history',
        verbose_name=_('Location Id')
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name='book_histories',
        related_query_name='book_history',
        verbose_name=_('Location Id')
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.PROTECT,
        related_name='book_histories',
        related_query_name='book_history',
        verbose_name=_('Publisher Id')
    )
    genres = models.ManyToManyField(
        Genre,
        related_name='book_histories',
        related_query_name='book_history',
        verbose_name=_('Genre Id')
    )
    languages = models.ManyToManyField(
        Language,
        related_name='book_histories',
        related_query_name='book_history',
        verbose_name=_('Language Id')
    )
    writers = models.ManyToManyField(
        Writer,
        related_name='book_histories',
        related_query_name='book_history',
        through='BookWriterHistory',
        verbose_name=_('Writer Id')
    )
    # Fields
    name = models.CharField(
        _('Book Name'),
        max_length=100,
        help_text=_("Name of the book.")
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        help_text=_("Description about the book.")
    )
    year = models.DateField(
        _('Publish Year'),
        blank=True,
        null=True,
        help_text=_('Year of the publishing the book.')
    )
    edition_number = models.IntegerField(
        _('Edition Number'),
        blank=True,
        null=True,
        help_text=_('Number of the book edition.')
    )
    volume = models.IntegerField(
        _('Volume Number'),
        blank=True,
        null=True,
        help_text=_('Number of the book volume.')
    )
    part = models.IntegerField(
        _('Part Number'),
        blank=True,
        null=True,
        help_text=_('Number of the book part.')
    )
    page_quantity = models.IntegerField(
        _('Page Quantity'),
        blank=True,
        null=True,
        help_text=_('Quantity of the book pages.')
    )
    is_copyright = models.BooleanField(
        _('Is copyright?'),
        default=False,
        help_text=_('For determine if the book is copyrighted ')
    )
    image = models.ImageField(
        _('Image'),
        default='default_book.jpg',
        upload_to='book_pics',
        help_text=_('Picture of the book.')
    )
    timestamp = models.DateTimeField(
        _('Created Timestamp'),
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('book history ')
        verbose_name_plural = _('book histories')

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
        # return reverse('book-detail', kwargs={'pk': self.pk})

    # OTHER METHODS


# many to many table through
class BookWriterHistory(models.Model):
    book_history = models.ForeignKey(BookHistory, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.PROTECT)
    writer = models.ForeignKey(Writer, on_delete=models.PROTECT)
