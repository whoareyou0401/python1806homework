from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from email_veryfi import myutil
from django.core.cache import cache
# Create your views here.
def get_verify_code(req):
    param = req.GET
    email = param.get('email')
    name = param.get('name')
    #验证邮箱的合法性
    #验证这个邮箱是否在我们的系统中已经注册了



    #生成验证码
    token = myutil.get_token()
    #拼接验证链接
    verify_url = "http://123.207.170.75:12345/verify/" + token
    #保存验证码
    cache.set(token, email, 60)
    print(cache.get(token))
    #发邮件
    title = "欢迎注册"
    message = "请将如下链接复制到浏览器访问{url}".format(
        url=verify_url
    )
    email_from = "648328530@qq.com"
    send_mail(title,message,email_from,[email])
    return HttpResponse("注册成功，请查看激活邮件")

def verify(req,token):
    email = cache.get(token)
    print(email)
    if email:
        return HttpResponse("修改用户状态，可以使用了"+email)
    else:
        return HttpResponse("验证链接不正确")


