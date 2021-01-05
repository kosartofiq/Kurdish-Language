from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home/home.html'

class AboutPageView(TemplateView):
    template_name = 'home/about.html'