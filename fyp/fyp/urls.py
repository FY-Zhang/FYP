from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('photos', views.photos, name='photos'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('forum', views.forum, name='forum'),
    path('post', views.post, name='post'),
    path('send_post', views.send_post, name='send_post'),
    path('my_post', views.my_post, name='my_post'),
    path('delete_post', views.delete_post, name='delete_post'),
]