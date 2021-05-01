from django.shortcuts import render
from django.http import request, HttpResponse

# Create your views here.


def basic(request):
    return HttpResponse("this is the basic view of todo")
