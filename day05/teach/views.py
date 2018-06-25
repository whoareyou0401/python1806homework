from datetime import timedelta

from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def index(req):
    print("*****req****************")
    print(dir(req))
    print("******req.META***************")
    print(req.META.get("REMOTE_ADDR"))
    print("****req.method)********")
    print(req.method)
    return HttpResponse("ok")


def my_response(request):
    response = HttpResponse()
    response.content = "我是ontent设置的"

    response.write("这个是write")
    response.flush()
    response.status_code = 404
    return response


def my_json(req):
    rice_list = ["米饭", '炒饼', '腰子', '炒韭菜']
    res = {
        'data': rice_list,
        'code': 1,
        'msg': 'ok',

    }
    return JsonResponse(res)


# 首页--用户系统
def t5_index(req):
    u_name = req.session.get("u_name")
    return render(req, 't5_index.html', context={"u_name": u_name})


def logout(req):
    req.session.flush()
    return HttpResponse("退出成功")


def login(req):
    if req.method == "GET":
        return render(req, 'login.html')
    elif req.method == "POST":
        param = req.POST
        name = param.get("name")
        pwd = param.get("pwd")
        # 校验先不做了
        response = HttpResponse("登录成功")
        req.session["u_name"] = name
        # response.set_cookie("u_name",name)
        # response.set_cookie("u_name",name,expires=timedelta(seconds=10))
        # req.session['111']='lelele'
        return response
