# coding=utf-8
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.generic.base import View
import cloudsight
import time
import os
import json
from .models import IMG,WeixinToken,UserImg
from django.shortcuts import render

class IndexView(View):
    def get(self,request):
        return render(request, 'AI/index.html', {
            'code': 200,
        })
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

    @csrf_exempt
    def post(self,request):
        img = request.FILES.get('picture')
        if img is None:
            return HttpResponse('You need upload a picture!')
        auth = cloudsight.SimpleAuth('nSmkfLGwl4-yW1s-swKoXA')
        # 8u3iemtYYiIcFaZOK1E4QA
        api = cloudsight.API(auth)
        InputFile = img.name
        response = api.image_request(img, InputFile, {'image_request[locale]': 'zh-CN','image_request[language]':'zh-CN' })
        status = api.wait(response['token'], timeout=30)
        userImg = UserImg(
            name = status['name'],
            url = status['url'],
        )
        data = {
            'name':status['name'],
            'url':status['url'],
            'code':200,
        }
        userImg.save()
        return  HttpResponse(json.dumps(data),content_type="application/json;charset=utf-8")


class UploadImgView(View):
    @csrf_exempt
    def get(self,request):
        return render(request, 'img_tem/uploadimg.html')

    @csrf_exempt
    def post(self,request):
        img = request.FILES.get('img')
        if img is None:
            return HttpResponse('You need upload a picture!')
        auth = cloudsight.SimpleAuth('nSmkfLGwl4-yW1s-swKoXA')
        api = cloudsight.API(auth)
        InputFile = img.name
        print(InputFile)
        response = api.image_request(img, InputFile, {'image_request[locale]': 'zh-CN','image_request[language]':'zh-CN'})
        print(response)
        status = api.wait(response['token'], timeout=30)
        data = {
            'name':status['name'],
            'url':status['url'],
            'code':200,
        }
        return HttpResponse(json.dumps(data),content_type='application/json;charset=utf-8')

@csrf_exempt
def showImg(request):
    imgs = IMG.objects.all()
    content = {
        'imgs':imgs,
    }
    for i in imgs:
        print i.img.url
    return render(request, 'img_tem/showimg.html', content)