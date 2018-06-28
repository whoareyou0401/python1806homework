from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from email_ver import myutil
from django.core.cache import cache
# Create your views here.



def get_verify_code(req):
    param = req.GET
    email = param.get('email')
    name = param.get('nmae')
    # 1 生成验证码
    token = myutil.get.token()
    verify_url = "http://39.106.147.156/verify/" + token
    # 2 保存验证码
    cache.set(token, email, 60)
    # 3 发送邮件
    title = "欢迎注册会员"
    message = "请将如下连接复制到浏览器访问{url}".format(url=verify_url)
    email_from = '69189668@qq.com'
    # send_mail 是个函数
    send_mail(title, message, email_from, [email])
    return HttpResponse('注册成功，请看激活邮件')

def verify(req,token):
    # 取数据库找对应的人
    email = cache.get(token)
    if email:
        return HttpResponse('修改用户状态，可以使用'+email)
    else:
        return HttpResponse('验证连接不正确')