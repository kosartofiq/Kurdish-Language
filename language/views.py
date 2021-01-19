from django.views.generic import ListView

from .models import Language


class LanguageListView(ListView):
    model = Language
    context_object_name = 'languages'
    ordering = ['name']