#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/7/6 15:01

import requests
import json


response = requests.get('http://fanyi.youdao.com/openapi.do?keyfrom=11pegasus11&key=273646050&type=data&doctype=json&version=1.1&q=country')

data = json.loads(response.content)
print(data['translation'])