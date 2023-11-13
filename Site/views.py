import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Comment
from users.models import Profile


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


@login_required
def comment_page(request):
    comments = Comment.objects.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('comment_page')

    return render(request, 'Site/comments.html', {'form': form, 'comments': comments})
