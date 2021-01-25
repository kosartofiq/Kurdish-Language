from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.utils.translation import ugettext as _

from .models import Genre, GenreHistory, Job, JobHistory, Location, LocationHistory


def library(request):
    return render(request, 'library/library.html')


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




