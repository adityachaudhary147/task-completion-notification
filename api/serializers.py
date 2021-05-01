from rest_framework import serializers
from todo.models import Task,Notification
from rest_framework.exceptions import APIException


class AccessUnavailable(APIException):
    status_code = 403
    default_detail = 'Access Denied'
    default_code = 'service_unavailable'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['customer','time']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        exclude = []
