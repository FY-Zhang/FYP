# Generated by Django 3.1.2 on 2021-03-05 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Model', '0012_auto_20210305_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField(default=0)),
                ('post_title', models.CharField(max_length=200)),
                ('post_topic', models.CharField(max_length=50)),
                ('post_content', models.TextField()),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('user_email', models.CharField(max_length=50)),
                ('like_num', models.IntegerField(default=0)),
                ('comment_num', models.IntegerField(default=0)),
                ('collection_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField(default=0)),
                ('user_email', models.CharField(max_length=50)),
                ('comment_id', models.IntegerField(default=0)),
                ('comment_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User_Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=50)),
                ('post_id', models.IntegerField(default=0)),
                ('collection_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
