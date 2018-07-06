# coding=utf-8
from django.shortcuts import render


from django.http import HttpResponse
from django.views.generic.base import View


class IndexView(View):
    def get(self,request):
        return HttpResponse("it's ok!")


class UploadView(View):

    def get(self,request):
        return HttpResponse('this is get method')

    def post(self,request):
        return HttpResponse('this is post method')


def upload(request):
    if request.method == 'POST':
        return HttpResponse('This is POST!')
    else:
        return HttpResponse('Hello world!')
