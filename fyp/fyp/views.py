from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def article(request):
    return render(request, 'article.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def forum(request):
    return render(request, 'forum.html')

def send_post(request):
    return render(request, 'send_post.html')