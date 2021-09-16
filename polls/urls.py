from django.urls import path
from . import views


app_name = "polls"


urlpatterns = [
    path(
        route="list/",
        view=views.poll_list,
        name="poll_list"),
    path(
        route="detail/<int:pk>/",
        view=views.poll_detail,
        name="poll_detail")
]
