from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'basic.html')

def about(request):
    return render(request,'tut17.html')