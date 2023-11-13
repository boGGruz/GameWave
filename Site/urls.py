from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("profile/", views.profile, name="profile"),
    path("doom/", views.doom, name="doom"),
    path("duke/", views.duke, name="duke"),
    path("wolf/", views.wolf, name="wolf"),
    path("mk/", views.mk, name="mk"),
    path("doom2/", views.doom2, name="doom2"),
    path("mario/", views.mario, name="mario"),
    path("shadow-warrior/", views.shadow_warrior, name="shadow-warrior"),
    path("heroes/", views.heroes, name="heroes"),
    path("comment_page/", views.comment_page, name="comment_page"),
]
