from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import Language, LanguageHistory


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
