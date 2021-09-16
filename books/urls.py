from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path(
        route="all/", 
        view=views.BookListGenericView.as_view(), 
        name="all"),
]
