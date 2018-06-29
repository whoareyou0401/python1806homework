from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from m import myutil
from django.core.cache import cache
# Create your views here.


def get_code(req):
    param = req.GET
    email = param.get('email')
    name = param.get('name')
    token = myutil.get_token()
    verify_url = "http://47.105.111.162:12348/verify/" + token
    cache.set(token,email,300)
    title = "欢迎注册会员"
    message = "复制以下连接到到浏览器{url}".format(
        url = verify_url
    )
    email_from = "493024318@qq.com"
    send_mail(title,message,email_from,[email])
    return HttpResponse('ok')

def zxc(req,qwe):
    email = cache.get(qwe)
    if email:
        return HttpResponse("可以使用" + email)
    else:
        return HttpResponse("不正确")


