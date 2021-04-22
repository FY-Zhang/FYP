from django.db import models

# Create your models here.

class User(models.Model):
    user_email = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_type = models.IntegerField(default=0)  #默认普通用户，1是管理员

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_topic = models.CharField(max_length=50)
    post_content = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True) #发帖时间
    user_email = models.CharField(max_length=50)

class Post_Comment(models.Model):
    post_id = models.IntegerField(default=0)
    user_email = models.CharField(max_length=50)
    comment_content = models.TextField()