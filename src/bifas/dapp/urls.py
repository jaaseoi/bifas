from django.urls import path

from . import views

urlpatterns = [
    path(
        route="",
        view=views.index,
        name="index",
    ),
    path(
        route="index",
        view=views.index,
    ),
    path(
        route="ping",
        view=views.ping,
        name="ping",
    ),
]