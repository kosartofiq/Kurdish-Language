from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import Language, LanguageHistory, Dialect, DialectHistory
from .forms import DialectCreateForm


class LanguageListView(ListView):
    model = Language
    context_object_name = 'languages'
    ordering = ['name']


class LanguageCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Language
    fields = ['name', 'native_name', 'iso_639_1', 'iso_639_2', 'description']
    success_message = _(f'New language was created successfully.')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class LanguageDetailView(DetailView):
    model = Language


def language_histories(request, pk):
    language = Language.objects.get(pk=pk)
    histories = LanguageHistory.objects.filter(language=language).order_by('-timestamp')
    rendered_histories_html = render_to_string('language/language_histories.html', {'histories': histories})
    return_json_data = {
        'histories_html': rendered_histories_html,
    }
    return JsonResponse(return_json_data)


class LanguageUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Language
    fields = ['name', 'native_name', 'iso_639_1', 'iso_639_2', 'description']
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


def dialect_list_view(request, pk, dialect_pk=None):
    language = Language.objects.get(pk=pk)
    dialects = Dialect.objects.filter(language=language, super_dialect=dialect_pk).order_by('name')
    # create breadcrumbs to dig in dialects
    breadcrumbs = []
    # if we get pk2, it means it ask for detail a dialect not dialect
    if dialect_pk:
        # get current dialect
        loop = Dialect.objects.get(pk=dialect_pk)
        # if found
        if loop:
            # add to breadcrumbs
            breadcrumbs.append(loop)
            # while current dialect has super dialect
            while loop.super_dialect:
                # add to breadcrumbs
                breadcrumbs.append(loop.super_dialect)
                # make super dialect to current dialect
                loop = loop.super_dialect
            # reverse arrangement
            breadcrumbs.reverse()
    context = {
        'language': language,
        'dialects': dialects,
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'language/dialect_list.html', context)


@login_required
def dialect_create_view(request, language_pk, dialect_pk=None, instance=None):
    language = Language.objects.get(pk=language_pk)
    # if dialect created under another dialect
    dialect = None
    if dialect_pk:
        dialect = Dialect.objects.get(pk=dialect_pk)

    # post request , it means filled data , or we create new fresh one
    if request.method == 'POST':
        form = DialectCreateForm(language, request.POST)
        if form.is_valid():
            form.instance.creator = request.user
            form.instance.language = language
            form.save()
            messages.success(request, f'New dialect has added successfully.')
            return redirect('dialect-detail', pk1=language.id, pk2=form.instance.id)
    else:
        form = DialectCreateForm(language, initial={'super_dialect': dialect})
    context = {
        'form': form,
        'language': language,
        'dialect': dialect,
        'update': False
    }
    return render(request, 'language/dialect_form.html', context)

