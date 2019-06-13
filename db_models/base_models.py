# -*- coding: utf-8 -*-
#!/usr/bin/env python3


from django.db import models

class BaseModels(models.Model):
    """抽象基类"""
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        abstract = True
