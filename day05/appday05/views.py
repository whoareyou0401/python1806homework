from datetime import timedelta

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


def index(req):
    # print(dir(req))
    print(req.META.get("REMOTE_ADDR"))
    print(req.method)
    return HttpResponse('ok')


def my_response(request):
    response = HttpResponse()
    response.cotnect = "我是content设置的"
    response.write("这个是write")
    response.flush()
    response.status_code = 404
    return response


def my_json(req):
    rice_list = ["米饭", "炒饼", '腰子', "烤肉"]
    res = {"data": rice_list, "code": 1, "msg": "ok"}
    return JsonResponse(res)


def t5_index(req):
    u_name = req.COOKIES.get('u_name')
    return render(
        req,
        "t5_index.html",
        context={"u_name": u_name}
    )


def logout(req):
    response = HttpResponse("ok")
    response.delete_cookie("u_name")
    return response


def login(req):
    if req.method == "GET":
        return render(req, 'login.html')
    elif req.method == "POST":
        param = req.POST
        name = param.get("name")
        pwd = param.get('pwd')

        response = HttpResponse("登录成功")
        # response.set_cookie('u_name', name, max_age=6)
        # response.set_cookie("u_name", name, expries=timedelta(seconds=10))
        # req.session["ll"] = "lelele"
        return response


