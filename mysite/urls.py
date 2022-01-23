"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todo.views import homeView, addTodo, deleteTodo, doneTodo, coverImage, logout_request, register_request, selectClient, addActivity, streamView

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', homeView, name='home'),
    path('stream', streamView),
    path('addTodo/', addTodo),
    path('addActivity/', addActivity),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('doneTodo/<int:todo_id>/', doneTodo),
    path('selectClient/<int:client_id>/', selectClient),
    path('app.png', coverImage),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path("register", register_request, name="register"),
    path("logout", logout_request, name="logout")
]