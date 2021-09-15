from django.shortcuts import render
from django.views import generic
from . import models


class BookListGenericView(generic.ListView):
    model = models.Book
    template_name = 'books/books_list.html'
