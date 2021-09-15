from rest_framework import generics
from books import models as books_models
from . import serializers as book_serializers


class ListBooksAPIView(generics.ListAPIView):
    serializer_class = book_serializers.BooksSerializer
    queryset = books_models.Book.objects.all()

