from django.contrib import auth
from django.shortcuts import render
# 用来写请求处理逻辑的
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# django处理过程
# 1，url指定路径/hello
# 2,setting.py找到url的配置文件
def hello(request):
    return render(request, "hello.html")


def login(request):
    '''用户登录'''

    # 返回登录页面
    if request.method == "GET":
        return render(request, "loogin.html", {"error": ""})

    print("请求方法", request.path)

    # 处理登录请求
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "" or password == "":
            return render(request, "loogin.html", {
                "error": "用户名或密码为空！"
            })
        user = auth.authenticate(username=username, password=password)
        print("用户是否存在", user)

        if user is not None:
            auth.login(request, user)  # 记录登录状态
            return HttpResponseRedirect("/manage/")  # 如果登录成功重定向到manage页面
        else:
            return render(request, "loogin.html", {
                "error": "用户名或密码错误！"
            })


@login_required
def manage(request):
    '''接口管理'''
    return render(request, "manage.html")


def logout(request):
    '''退出'''
    auth.logout(request)
    return HttpResponseRedirect("/")
