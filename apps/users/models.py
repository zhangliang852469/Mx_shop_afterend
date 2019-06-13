from django.db import models
from django.contrib.auth.models import AbstractUser

from db_models.base_models import BaseModels

# Create your models here.


class UserProfile(BaseModels, AbstractUser):
    """ 用户 """
    CHOICES_GENDER = (
        ('male', '男'),
        ('female', '女'),
    )
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='姓名')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月')
    gender = models.CharField(choices=CHOICES_GENDER, max_length=6, default='female',
                              verbose_name='性别')
    mobile = models.CharField(max_length=11, verbose_name='电话')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='邮箱')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(BaseModels, models.Model):
    """短信验证码"""
    code = models.CharField(max_length=10, verbose_name='验证码')
    mobile = models.CharField(max_length=11, verbose_name='电话')

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code




