# coding=utf-8
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.generic.base import View
import cloudsight
import time
import os
import json
from .models import IMG,WeixinToken
import requests

class IndexView(View):
    def get(self,request):
        return HttpResponse("it's ok!")

class WeixinView(View):
    def get(self,request):

        signature = request.GET.get('signature','')
        timestamp = request.GET.get('timestamp', '')
        nonce = request.GET.get('nonce', '')
        echostr = request.GET.get('echostr', '')
        new_weixin_token = WeixinToken(
            signature = signature ,
            timestamp = timestamp,
            nonce = nonce,
            echostr = echostr,
        )
        new_weixin_token.save()
        data = {
            'echostr':echostr,
        }
        return HttpResponse(echostr, content_type="application/json")
class UploadView(View):

    def get(self,request):
        return HttpResponse('this is get method')

    def post(self,request):
        img = request.FILES.get('picture')
        if img is None:
            return HttpResponse('You need upload a picture!')
        auth = cloudsight.SimpleAuth('8h9ANlD_Gy8PkvMhUXUn1Q')
        api = cloudsight.API(auth)
        InputFile = img.name
        response = api.image_request(img, InputFile, {'image_request[locale]': 'en-US', })
        status = api.wait(response['token'], timeout=30)
        fanyi_res = requests.get('http://fanyi.youdao.com/openapi.do?keyfrom=11pegasus11&key=273646050&type=data&doctype=json&version=1.1&q='+status['name'])
        return  HttpResponse(fanyi_res)
        # return  HttpResponse(str(status['name']))


@csrf_exempt
def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img'),
            name = request.FILES.get('img').name
        )
        img = request.FILES.get('img')
        if img is None:
            return HttpResponse('You need upload a picture!')
        auth = cloudsight.SimpleAuth('8h9ANlD_Gy8PkvMhUXUn1Q')
        api = cloudsight.API(auth)
        InputFile = img.name
        response = api.image_request(img, InputFile, {'image_request[locale]': 'en-US', })
        status = api.wait(response['token'], timeout=30)
        new_img.url = status['url']
        new_img.save()
        fanyi_res = requests.get('http://fanyi.youdao.com/openapi.do?keyfrom=11pegasus11&key=273646050&type=data&doctype=json&version=1.1&q='+status['name'])

        return  HttpResponse(fanyi_res)
    else:
        return render(request, 'img_tem/uploadimg.html')

@csrf_exempt
def showImg(request):
    imgs = IMG.objects.all()
    content = {
        'imgs':imgs,
    }
    for i in imgs:
        print i.img.url
    return render(request, 'img_tem/showimg.html', content)