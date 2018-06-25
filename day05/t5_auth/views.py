from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from t5_auth.auth import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def register(req):
    if req.method == "GET":
        return render(req, "register.html")
    elif req.method == "POST":
        params = req.POST
        name = params.get("user_name")
        pwd = params.get("pwd")
        confirm_pwd = params.get("confirm_pwd")
        # 根据产品需求 账号密码校验
        if name and len(name) > 3 and pwd and len(pwd) > 6 and pwd == confirm_pwd:
            # 保存用户，密码
            User.objects.create_user(username=name, password=pwd)
            return redirect(reverse("t5_auth:login"))
        else:
            return HttpResponse("账号或密码有误")


def login_api(req):
    if req.method == "GET":
        return render(req, 't5_auth_login.html')
    elif req.method == "POST":
        # 获取下一个跳转页面
        # next = req.GET.get("next")
        # print(next)
        params = req.POST
        name = params.get("username")
        pwd = params.get("pwd")
        # django自带的认证 认证用户
        user = authenticate(username=name, password=pwd)
        if user:
            # django自带的login,取的时候是req.user
            login(req, user)
            # if next:
            #     return redirect(next)
            # else:
            #     # 认证成功返回到首页
            return redirect(reverse("t5_auth:index"))
        # 认证失败
        else:
            return HttpResponse("账号密码不对")


@login_required(login_url="/t5_auth/login")
def welcome_vip(req):
    username = req.user
    print(username)
    data = {
        'username': username
    }
    return render(req, 'welcom.html', context=data)


def index(req):
    u_name = req.user
    if u_name.is_anonymous():
        u_name = "无人登录"
    data = {
        "u_name": u_name
    }
    return render(req, 't5_auth_index.html', context=data)


def logout(req):
    req.session.flush()
    return HttpResponse("退出成功")
