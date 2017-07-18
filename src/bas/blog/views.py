from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html',locals())

def search(request):
    return render(request, 'search_result.html',locals())

def author(request):
    return render(request, 'author.html',locals())

def book_info(request):
    return render(request, 'book_info.html',locals())

def publish_info(request):
    return render(request, 'publish_info.html',locals())

