# Generated by Django 3.1.2 on 2021-03-05 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0008_auto_20210305_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='post_comment',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='user_collection',
            name='user_id',
        ),
    ]