from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    return render(request, 'Site/catalog.html')


def about(request):
    return render(request, 'Site/about.html')


def profile(request):
    return render(request, 'Site/profile.html')


def doom(request):
    return render(request, 'Site/doom.html')


def duke(request):
    return render(request, 'Site/duke.html')


def wolf(request):
    return render(request, 'Site/wolf.html')


def mk(request):
    return render(request, 'Site/mk.html')


def doom2(request):
    return render(request, 'Site/doom2.html')


def mario(request):
    return render(request, 'Site/mario.html')


def shadow_warrior(request):
    return render(request, 'Site/shadow-warrior.html')


def heroes(request):
    return render(request, 'Site/heroes.html')


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Site/catalog.html', context)
