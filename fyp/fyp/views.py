from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def forum(request):
    return render(request, 'forum.html')

def send_post(request):
    return render(request, 'send_post.html')