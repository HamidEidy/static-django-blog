from django.http import HttpResponse
from django.shortcuts import render
def index(req):
    return render(req, 'blogs/index.html')

def posts(req):
    return render(req, 'blogs/all-posts.html')

def single_post(req):
    return HttpResponse('single')