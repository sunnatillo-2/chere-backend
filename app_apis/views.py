from rest_framework import generics
from rest_framework.response import Response

from app_tados.models import Todo
from .serializers import TodoSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class AllTodoList(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDelete(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def destry(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print(f"Delete | Todo title: {instance}"))


class TodoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    partial = True
