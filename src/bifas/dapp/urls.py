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

    # -------------------------------- Mempool --------------------------------
    path(
        route="mempool_index_page",
        view=views.mempool_index_page,
        name="mempool_index_page",
    ),
    path(
        route="mempool_get",
        view=views.mempool_get,
        name="mempool_get",
    ),
    path(
        route="mempool_post",
        view=views.mempool_post,
        name="mempool_post",
    ),
]