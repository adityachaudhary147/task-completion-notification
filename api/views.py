from django.shortcuts import render
from django.http import request, HttpResponse
from rest_framework import generics,permissions
# Create your views here.
from .serializers import TaskSerializer,AccessUnavailable
from todo.models import Task,Notification
from accounts.models import Customer,Moderator

from rest_framework.decorators import api_view
from api.serializers import TaskSerializer, NotificationSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

#  return all task related to the user
@api_view(['GET'])
def tasklist(request):
    if request.method == 'GET':
        we=Customer.objects.filter(user=request.user)
        if len(we)==0:
            raise AccessUnavailable()
        tasks = Task.objects.filter(customer=we[0])
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

#  return all task related to the user


@api_view(['GET'])
def taskcreatedlist(request):
    if request.method == 'GET':
        we = Customer.objects.filter(user=request.user)
        if len(we) == 0:
            raise AccessUnavailable()
        tasks = Task.objects.filter(customer=we[0],status=1)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def taskfinishedlist(request):
    if request.method == 'GET':
        we = Customer.objects.filter(user=request.user)
        if len(we) > 0:
            raise AccessUnavailable()
        tasks = Task.objects.filter(finished_by=request.user, status=2)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def taskfinishedandsubmittedlist(request):
    if request.method == 'GET':
        we = Customer.objects.filter(user=request.user)
        if len(we) > 0:
            raise AccessUnavailable()
        tasks = Task.objects.filter(finished_by=request.user, status=3)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def tasksubmittedlist(request):
    if request.method == 'GET':
        we = Customer.objects.filter(user=request.user)
        if len(we) == 0:
            raise AccessUnavailable()
        tasks = Task.objects.filter(customer=we[0], status=3)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    title = models.CharField(max_length=100)
    details = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='created_by')

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='1')

@api_view(['POST'])
def taskcreate(request):
    if request.method == 'POST':
        we = Customer.objects.filter(user=request.user)
        if len(we) == 0:
            raise AccessUnavailable()
        data = {'title': request.data.get('title'), 'details': request.data.get(
            'details') }
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            er=serializer.save(customer=we[0])
            for r in Moderator.objects.all():
                tr=User.objects.filter(id=r.user.id)
                Notification.objects.create(sender=request.user, recipient=tr[0],message="Task {fname}, Created by  {age} ".format(fname=er.id , age=request.user.username))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def notificationlist(request):
    if request.method == 'GET':
        notis = Notification.objects.filter(recipient=request.user)
        serializer = NotificationSerializer(notis, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def taskfinish(request):
    if request.method == 'POST':
        we = Customer.objects.filter(user=request.user)
        if len(we)>0:
            raise AccessUnavailable()
        task_id=request.data.get('id')
        task_id=int(task_id)

        er=Task.objects.filter(id=task_id)
        if len(er)==0:
            return Response("No task found")
        if int(er[0].status)!=1:
            return Response(" Task is not in Created State ")
        serializer = TaskSerializer(er[0], data={'status': '2'}, partial=True)
        if serializer.is_valid():
            ertt = serializer.save(finished_by=request.user)
            for r in Customer.objects.filter(id=er[0].customer.id):
                tr = User.objects.filter(id=r.user.id)
                Notification.objects.create(sender=request.user, recipient=tr[0], message="Task {fname}, Completed  {age} ".format(fname=ertt.id, age=request.user.username),related_task=ertt)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def tasksubmit(request):
    if request.method == 'POST':
        we = Customer.objects.filter(user=request.user)
        if len(we) == 0:
            raise AccessUnavailable()
        task_id = request.data.get('id')
        task_id = int(task_id)
        er = Task.objects.filter(id=task_id)
        if len(er) == 0:
            return Response("No task found")
        if int(er[0].status) != 2:
            return Response(" Task is not in Finished State ")
        serializer = TaskSerializer(er[0], data={'status': '3'}, partial=True)
        if serializer.is_valid():
            ertt = serializer.save()
            for r in Customer.objects.filter(id=er[0].customer.id):
                tr = User.objects.filter(id=r.user.id)
                Notification.objects.create(sender=request.user, recipient=tr[0], message="Task {fname}, Submitted By YOu {age} ".format(
                    fname=ertt.id, age=request.user.username), related_task=ertt)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def basic(request):
    return HttpResponse("this is the basic view of api")
