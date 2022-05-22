from django.shortcuts import render
# 用来写请求处理逻辑的
# Create your views here.
from django.http import HttpResponse


# django处理过程
# 1，url指定路径/hello
# 2,setting.py找到url的配置文件
def hello(requests):
    return render(requests,"hello.html")


