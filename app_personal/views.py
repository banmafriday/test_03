from django.shortcuts import render
# 用来写请求处理逻辑的
# Create your views here.
from django.http import HttpResponse


# django处理过程
# 1，url指定路径/hello
# 2,setting.py找到url的配置文件
def hello(request):
    return render(request, "hello.html")


def login(request):
    '''用户登录'''
    if request.method == "GET":
        return render(request, "login.html", {"error": "登录页面"})


def login_account(request):
    '''登录动作的处理'''
    print("请求方法", request.path)
    if request.method == "GET":
        username = request.GET.get("username", "")
        password = request.GET.get("password", "")
        print('>>>', username, type(username))
        print('>>>', username, type(password))
        if username == "" or password == "":
            return render(request, "login.html", {
                "error": "用户名或密码为空！"
            })

        if username == "banma" and password == "123":
            return render(request, "login.html", {
                "error": "登录成功！"
            })
        else:
            return render(request, "login.html", {
                "error": "用户名或密码错误！"
            })
