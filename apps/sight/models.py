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

class WeixinToken(models.Model):
    signature = models.CharField(max_length=500,default='')
    timestamp = models.CharField(max_length=500,default='')
    nonce = models.CharField(max_length=500,default='')
    echostr = models.CharField(max_length=500,default='')
    token = models.CharField(max_length=500,default='')
    class Meta:
        verbose_name = u'微信Token'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.echostr

class UserImg(models.Model):
    name = models.CharField(max_length=500,default='')
    url = models.CharField(max_length=500,default='')
    translate = models.CharField(max_length=500,default='')
    class Meta:
        verbose_name = u'图片信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name