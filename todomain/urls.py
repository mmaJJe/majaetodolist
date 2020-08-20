from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.createTodo, name="create"),
    path('toggle/<int:pk>', views.toggleTodo, name="toggle"),
    path('delete/<int:pk>', views.deleteTodo, name="delete"),
]
