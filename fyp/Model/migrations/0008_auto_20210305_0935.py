# Generated by Django 3.1.2 on 2021-03-05 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0007_post_post_comment_user_user_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_comment',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='user_collection',
            name='user_email',
        ),
        migrations.AddField(
            model_name='post',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post_comment',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_collection',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
