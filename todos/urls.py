from django.contrib import admin
from django.urls import path, include
from . import views
from .views import todo, todos, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/<int:todoId>/', todo, name="todo"),
    path('todos/', todos, name="todos"),
    path('', home),
]
