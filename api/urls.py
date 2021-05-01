"""rest_notify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [

    path('', views.basic, name='basic-api'),
   
        path('todo/all',views.tasklist,name='todo-all'),
    path('todo/created', views.taskcreatedlist, name="todo-create"),
    path('todo/finished', views.taskfinishedlist, name="todo-finished"),
    path('todo/finishedandsubmitted', views.taskfinishedandsubmittedlist, name="todo-finished-sub"),
    path('todo/submitted', views.tasksubmittedlist, name='todo-created'),

    path('todo/create', views.taskcreate, name='todo-create'),

    path('notify/all', views.notificationlist, name='notify-all'),
    path('todo/taskfinish',views.taskfinish,name='finish'),
    path('todo/tasksubmit', views.tasksubmit, name='submit'),
]
