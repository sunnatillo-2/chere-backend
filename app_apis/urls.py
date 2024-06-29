from django.urls import path

from .views import ListTodo, DetailTodo, AllTodoList, TodoDelete, TodoUpdate

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
    path('all/', AllTodoList.as_view()),
    path('del/<int:pk>/', TodoDelete.as_view()),
    path('update/<int:pk>/', TodoUpdate.as_view()),
]
