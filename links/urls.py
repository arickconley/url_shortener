from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("l/<guid>", views.single_link, name="link"),
    path("d/<guid>", views.details, name="details"),
    path("u", views.user_links, name="user-links"),
]
