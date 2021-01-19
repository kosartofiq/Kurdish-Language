from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext as _

from .models import Language


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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['historys'] = LanguageHistory.objects.filter(language=self.object.id).order_by('-timestamp')
        return context