from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("l/<guid>", views.single_link, name="link"),
]
