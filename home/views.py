from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('<h1>Kurdish Language Home ماڵپەڕی زمانی کوردی</h1>')


def about(request):
    return HttpResponse('<h1>Blog About دەربارەی بلۆگ</h1>')
