from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from . import myutil
from django.core.cache import cache
# Create your views here.
def get_verify_code(req):
    param = req.GET
    email = param.get('email')
    name = param.get('name')

    #生成验证码
    token = myutil.get_token()
    #拼接验证连接
    verify_url = "http://mhh4399.com:8888/verify"+token
    #保存验证码
    cache.set(token,email,60)
    #发送邮件
    title = "欢迎注册1806会员"
    message = "请将链接复制到浏览器访问{url}".format(
        url=verify_url
    )
    email_from = "912200556@qq.com"
    send_mail(title,message,email_from,[email])
    return HttpResponse("注册成功，请查看激活邮件")


def verify(req,token):
    email = cache.get(token)
    if email:
        return HttpResponse("修改用户状态，可以使用"+email)
    else:
        return HttpResponse("验证链接不正确")
