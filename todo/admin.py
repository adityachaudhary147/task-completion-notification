from django.contrib import admin

# Register your models here.
from todo.models import Notification,Task

admin.site.register(Notification)
admin.site.register(Task)