from django.shortcuts import render
from django.http import request,HttpResponse

# Create your views here.
def basic(request):
    return HttpResponse("this is the basic view of accounts")
def successlogin(request):
    return render(request,"loginsuccess.html")
def successlogout(request):
    return render(request,"logoutsuccess.html")
