from django.shortcuts import render

# Create your views here.

def library(request):
    return render(request, 'library/library.html')