# Generated by Django 3.1.2 on 2021-03-05 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0011_post_post_comment_user_user_collection'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Post_Comment',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='User_Collection',
        ),
    ]
