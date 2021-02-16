from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('article', views.article, name='article'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('forum', views.forum, name='forum'),
    path('send_post', views.send_post, name='send_post'),
]