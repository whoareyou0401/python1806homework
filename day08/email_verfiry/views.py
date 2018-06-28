from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from email_verfiry import myutil
from django.core.cache import cache
# Create your views here.
def get_verify_code(req):
    param = req.GET
    email = param.get('email')
    name = param.get("name")
    token = myutil.get_token()
    verify_url = "http://47.96.119.211:18468/verify/" + token
    cache.set(token,email,100)


    title = "欢迎注册1806会员"
    message = "赋值连接{url}".format(
        url = verify_url
    )
    email_from = "1846818768@qq.com"
    send_mail(title,message,email_from,[email])
    return HttpResponse("注册成功，请激活邮件")

def verify(req,token):
    email = cache.get(token)
    if email:
        return HttpResponse("修改用户状态，可以使用"+email)
    else:
        return ("验证不正确")