from rest_framework import generics

from .models import Todo
from .serializers import ToDoSerializers


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializers

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializers
