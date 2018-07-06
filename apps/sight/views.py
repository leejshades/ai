# coding=utf-8
from django.shortcuts import render


from django.http import HttpResponse


def upload(request):
    if request.method == 'POST':
        return HttpResponse('This is POST!')
    else:
        return HttpResponse('Hello world!')
