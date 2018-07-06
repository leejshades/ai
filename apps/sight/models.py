# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class IMG(models.Model):
    img = models.ImageField(upload_to='img/%Y/%m',default='image?default.png',max_length=500)
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=100,default='')
    class Meta:
        verbose_name = u'用户上传'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name