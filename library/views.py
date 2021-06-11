from library.models import book
from django import forms
from django.core.serializers import serialize
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.template.loader import render_to_string
from django.http import JsonResponse
import json
from django.utils.translation import ugettext as _

from global_functions import CleanSerializer
from language import models

from .models import Book, BookHistory, Page, Genre, GenreHistory, Job, JobHistory, Location, LocationHistory, Publisher, \
    PublisherHistory, Writer, WriterHistory
from language.models import Language

from .forms import BookCreateForm, PageCreateForm


# #########################
# Library
# #########################
class LibraryListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'library/library.html'
    ordering = ['name']


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        book = Book.objects.get(pk=self.kwargs['pk'])
        context['pages'] = Page.objects.filter(book=book).order_by('preview_page')
        return context


def book_histories(request, pk):
    book = Book.objects.get(pk=pk)
    histories = BookHistory.objects.filter(book=book).order_by('-timestamp')
    rendered_histories_html = render_to_string('library/book_histories.html', {'histories': histories})
    return_json_data = {
        'histories_html': rendered_histories_html,
    }
    return JsonResponse(return_json_data)


def page_detail(request):
    pass


@login_required
def page_create(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == 'POST':
        form = PageCreateForm(request.POST)
        if form.is_valid():
            form.instance.creator = request.user
            form.instance.book = book
            if form.save():
                return JsonResponse({
                    'msg': 'Success'
                })      
    else:
        form= PageCreateForm()
        rendered_page_create_from = render_to_string('library/page_form.html', {'form': form},request=request)

    return JsonResponse({'form':rendered_page_create_from})
    

class pageadd(CreateView):
    model = Page
    fields = ['book','number', 'page_type', 'preview_page','is_blank', 'is_finished', 'image']
    # form_class=BookCreateForm
    success_message = _(f'New page was created successfully.')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        book = Book.get(pk=1)
        form.isntance.book = book
        return super().form_valid(form)

class BookCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Book
    fields = ['location', 'publisher', 'genres', 'languages', 'writers', 'name', 'description', 'year',
              'edition_number', 'volume', 'part', 'page_quantity', 'is_copyright', 'image']
    # form_class=BookCreateForm
    success_message = _(f'New book was created successfully.')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


def book_form_datas(request):
    writers = Writer.objects.all().order_by('name')
    my_serializer = CleanSerializer()
    writers_name = my_serializer.serialize(writers, fields=['name'])
    #
    genres = Genre.objects.all().order_by('name')
    genres_name = my_serializer.serialize(genres, fields=['name'])
    #
    languages = Language.objects.all().order_by('name')
    languages_name = my_serializer.serialize(languages, fields=['name'])
    #
    locations = Location.objects.all().order_by('name')
    locations_name = my_serializer.serialize(locations, fields=['name'])
    #
    publishers = Publisher.objects.all().order_by('name')
    publishers_name = my_serializer.serialize(publishers, fields=['name'])

    return_json_data = {
        'writers_name': writers_name,
        'genres_name': genres_name,
        'languages_name': languages_name,
        'locations_name': locations_name,
        'publishers_name': publishers_name,
    }
    return JsonResponse(return_json_data)


class BookUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['location', 'publisher', 'genres', 'languages', 'writers', 'name', 'description', 'year',
              'edition_number', 'volume', 'part', 'page_quantity', 'is_copyright', 'image']
    success_message = _(f"Information was updated successfully.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['update'] = True
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


# #########################
# Genre
# #########################
class GenreListView(ListView):
    model = Genre
    context_object_name = 'genres'
    ordering = ['name']


class GenreDetailView(DetailView):
    model = Genre


def genre_histories(request, pk):
    genre = Genre.objects.get(pk=pk)
    histories = GenreHistory.objects.filter(genre=genre).order_by('-timestamp')
    rendered_histories_html = render_to_string('library/genre_histories.html', {'histories': histories})
    return_json_data = {
        'histories_html': rendered_histories_html,
    }
    return JsonResponse(return_json_data)


class GenreCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Genre
    fields = ['name', 'description']
    success_message = _(f'New genre was created successfully.')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class GenreUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Genre
    ['location', 'publisher', 'genres', 'languages', 'writers', 'name', 'description', 'year', 'edition_number',
     'volume', 'part', 'page_quantity', 'is_copyright', 'image']

    success_message = _(f"Information was updated successfully.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['update'] = True
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


# #########################
# Job
# #########################
class JobListView(ListView):
    model = Job
    context_object_name = 'jobs'
    ordering = ['name']


class JobDetailView(DetailView):
    model = Job


def job_histories(request, pk):
    job = Job.objects.get(pk=pk)
    histories = JobHistory.objects.filter(job=job).order_by('-timestamp')
    rendered_histories_html = render_to_string('library/job_histories.html', {'histories': histories})
    return_json_data = {
        'histories_html': rendered_histories_html,
    }
    return JsonResponse(return_json_data)


class JobCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Job
    fields = ['name', 'description']
    success_message = _(f'New job was created successfully.')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class JobUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Job
    fields = ['name', 'description']
    success_message = _(f"Information was updated successfully.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['update'] = True
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


# #########################
# Location
# #########################
class LocationListView(ListView):
    model = Location
    context_object_name = 'locations'
    ordering = ['name']


class LocationDetailView(DetailView):
    model = Location


def location_histories(request, pk):
    location = Location.objects.get(pk=pk)
    histories = LocationHistory.objects.filter(location=location).order_by('-timestamp')
    rendered_histories_html = render_to_string('library/location_histories.html', {'histories': histories})
    return_json_data = {
        'histories_html': rendered_histories_html,
    }
    return JsonResponse(return_json_data)


class LocationCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Location
    fields = ['name', 'description']
    success_message = _(f'New location was created successfully.')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class LocationUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Location
    fields = ['name', 'description']
    success_message = _(f"Information was updated successfully.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['update'] = True
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


# #########################
# Publisher
# #########################
class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'publishers'
    ordering = ['name']


class PublisherDetailView(DetailView):
    model = Publisher


def publisher_histories(request, pk):
    publisher = Publisher.objects.get(pk=pk)
    histories = PublisherHistory.objects.filter(publisher=publisher).order_by('-timestamp')
    rendered_histories_html = render_to_string('library/publisher_histories.html', {'histories': histories})
    return_json_data = {
        'histories_html': rendered_histories_html,
    }
    return JsonResponse(return_json_data)


class PublisherCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Publisher
    fields = ['name', 'description', 'logo']
    success_message = _(f'New publisher was created successfully.')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class PublisherUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Publisher
    fields = ['name', 'description', 'logo']
    success_message = _(f"Information was updated successfully.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['update'] = True
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


# #########################
# Writer
# #########################
class WriterListView(ListView):
    model = Writer
    context_object_name = 'writers'
    ordering = ['name']


class WriterDetailView(DetailView):
    model = Writer


def writer_histories(request, pk):
    writer = Writer.objects.get(pk=pk)
    histories = WriterHistory.objects.filter(writer=writer).order_by('-timestamp')
    rendered_histories_html = render_to_string('library/writer_histories.html', {'histories': histories})
    return_json_data = {
        'histories_html': rendered_histories_html,
    }
    return JsonResponse(return_json_data)


class WriterCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Writer
    fields = ['name', 'born_date', 'died_date', 'profile', 'image']
    success_message = _(f'New writer was created successfully.')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class WriterUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Writer
    fields = ['name', 'born_date', 'died_date', 'profile', 'image']
    success_message = _(f"Information was updated successfully.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['update'] = True
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
