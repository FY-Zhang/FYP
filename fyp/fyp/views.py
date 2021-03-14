from django.shortcuts import render, redirect
from Model import models

def index(request):
    return render(request, 'index.html')

def photos(request):
    return render(request, 'photos.html')

def login(request):
    status = request.COOKIES.get('is_login')
    if not status:
        cookie = ''
    else:
        cookie = status
    error_msg=''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # 判断数据库中是否有对应的账号密码
        ret = models.User.objects.filter(user_email=email, user_password=password)
        if ret:
            rep = redirect('/forum')
            rep.set_cookie("is_login", email)
            return rep
        else:
            error_msg = 'Wrong email or password'
            return render(request, 'login.html', {'error_msg': error_msg})
    return render(request, 'login.html', {'cookie': cookie})

def logout(request):
    rep = redirect('/forum')
    rep.delete_cookie("is_login")
    return rep

def register(request):
    status = request.COOKIES.get('is_login')
    if not status:
        cookie = ''
    else:
        cookie = status
    error_msg = ''
    if request.method == 'POST':
        user = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        user_list = models.User.objects.filter(user_email=email)
        if user_list:
            error_msg = 'Email has been registered'
            return render(request, 'register.html', {'error_msg': error_msg})
        elif password != confirmPassword:
            error_msg = 'Passwords are not same'
            return render(request, 'register.html', {'error_msg': error_msg})
        else:
            user = models.User.objects.create(user_email=email, user_name=user, user_password=password)
            user.save()
            return redirect('/login')
    return render(request, 'register.html', {'cookie': cookie})

def forum(request):
    posts = models.Post.objects.all().order_by('-id')   # 倒序取数据
    status = request.COOKIES.get('is_login')
    if not status:
        cookie = ''
    else:
        cookie = status
    return render(request, 'forum.html', {'cookie': cookie, 'posts': posts})

def post(request):
    status = request.COOKIES.get('is_login')
    # 读取帖子
    id = int(request.GET.get('id'))
    posts = models.Post.objects.all()
    for post in posts:
        if int(post.id == id):
            break
    users = models.User.objects.all()
    for user in users:
        if user.user_email == post.user_email:
            break
    if request.method == 'POST':
        # 存入评论
        if request.POST.get('commentBtn') == 'comment':
            comment = request.POST.get('comment')
            comments = models.Post_Comment.objects.create(post_id=id, user_email=status, comment_content = comment)
            comments.save()
            return redirect('/post?id='+str(id))
        # 修改帖子
        elif request.POST.get('editBtn') == 'edit':
            title = request.POST.get('title')
            topic = request.POST.get('topic')
            content = request.POST.get('content')
            models.Post.objects.filter(id=id).update(post_title=title, post_topic=topic, post_content=content, user_email=status)
            return redirect('/post?id='+str(id))
    # 读取评论
    post_comments = models.Post_Comment.objects.filter(post_id=id).order_by('-id')   # 倒序取数据
    # 获取Cookie
    if not status:
        cookie = ''
    else:
        cookie = status
    return render(request, 'post.html', {'post': post, 'user': user, 'status': status, 'cookie': cookie, 'users': users, 'post_comments': post_comments})

def send_post(request):
    status = request.COOKIES.get('is_login')
    if request.method == 'POST':
        title = request.POST.get('title')
        topic = request.POST.get('topic')
        content = request.POST.get('content')
        post = models.Post.objects.create(post_title=title, post_topic=topic, post_content=content, user_email=status)
        post.save()
        return redirect('/forum')
    
    if not status:
        cookie = ''
    else:
        cookie = status
    return render(request, 'send_post.html', {'cookie': cookie})

def my_post(request):
    status = request.COOKIES.get('is_login')
    posts = models.Post.objects.filter(user_email=status).order_by('-id')   # 倒序取数据
    if not status:
        cookie = ''
    else:
        cookie = status
    return render(request, 'my_post.html', {'cookie': cookie, 'posts': posts})

def delete_post(request):
    id = int(request.GET.get('id'))
    models.Post.objects.filter(id=id).delete()
    return redirect('/forum')