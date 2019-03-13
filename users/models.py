from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.

# 用户表
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    # verbose_name
    # 用户账号
    username = models.IntegerField()
    # 用户密码
    userpass = models.CharField(max_length=20)
    # 用户昵称
    nickname = models.CharField(max_length=15, unique=True, verbose_name='用户昵称')
    # 用户年龄
    age = models.IntegerField(3)
    # 用户性别
    gender = models.CharField(max_length=2, verbose_name='用户性别')
    # 用户头像
    header = models.ImageField(upload_to='static/images/headers/header.png', verbose_name='用户头像')
    # 用户电话
    phone = models.CharField(max_length=20,verbose_name='用户电话')
    # 用户邮箱
    email = models.EmailField(verbose_name='用户邮箱')
    # 注册时间
    regist_time = models.TimeField(auto_now_add=True, verbose_name='注册时间')
    # 上次登陆时间
    last_login_time = models.TimeField(auto_now_add=True, verbose_name='上次登陆时间')
    # 用户锁定状态0锁定 1 可用 2 删除
    status = models.IntegerField()
    # 建立系统系统内置用户关联一对一关系
    user = models.OneToOneField(User,on_delete=models.CASCADE)
# Create your models here.
