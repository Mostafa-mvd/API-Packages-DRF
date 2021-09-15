from rest_framework import generics
from . import models, serializers


class TodoListAPIView(generics.ListAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializers


class TodoDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializers
