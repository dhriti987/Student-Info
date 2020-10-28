from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'basic.html')

def contact(request):
    return HttpResponse('Contact')

def news(request):
    return HttpResponse('News')
    
def announce(request):
    return HttpResponse('Announcement')
    
def Profile(request):
    return render(request,'tut17.html')