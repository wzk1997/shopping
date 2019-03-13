# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-13 14:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.IntegerField()),
                ('userpass', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=15, unique=True, verbose_name='用户昵称')),
                ('age', models.IntegerField(verbose_name=3)),
                ('gender', models.CharField(max_length=2, verbose_name='用户性别')),
                ('header', models.ImageField(upload_to='static/images/headers/header.png', verbose_name='用户头像')),
                ('phone', models.CharField(max_length=20, verbose_name='用户电话')),
                ('email', models.EmailField(max_length=254, verbose_name='用户邮箱')),
                ('regist_time', models.TimeField(auto_now_add=True, verbose_name='注册时间')),
                ('last_login_time', models.TimeField(auto_now_add=True, verbose_name='上次登陆时间')),
                ('status', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
