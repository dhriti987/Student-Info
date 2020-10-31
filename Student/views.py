from django.shortcuts import render
from django.http import HttpResponse
from .News import News

# Create your views here.
def index(request):
    news = News()
    results = news.search_news('Education')
    print(results)
    params = {'News':results}
    return render(request,'home.html',params)