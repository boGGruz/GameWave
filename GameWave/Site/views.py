from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'Site/catalog.html')

def about(request):
    return render(request, 'Site/about.html')

def profile(request):
    return render(request, 'Site/profile.html')