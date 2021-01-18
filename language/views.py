from django.views.generic import ListView

from .models import Language


class LanguageListView(ListView):
    model = Language
    ordering = ['name']