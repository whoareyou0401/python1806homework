from django.core.mail import send_mail,send_mass_mail,EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def fa_you_jian(req):
    title = "offer"
    message = '啦啦啦'
    email_from = "493024318@qq.com"
    resc = ['493024318@qq.com','954502300@qq.com']
    send_mail(title,message,email_from,resc)
    return HttpResponse('发送成功')

def qun_fa(req):
    title1 = "1offer"
    message1 = '1啦啦啦'
    email_from = "493024318@qq.com"
    title = "2222offer"
    message = '2222啦啦啦'
    resc1 = ['493024318@qq.com']
    resc2 = ['954502300@qq.com','493024318@qq.com']
    senders1 = (title1,message1,email_from,resc1)
    senders2 = (title,message,email_from,resc2)
    send_mass_mail((senders1,senders2),fail_silently=False)
    return HttpResponse('YES')


def em(req):
    title = "3211offer"

    email_from = "493024318@qq.com"
    resc = ['493024318@qq.com']
    a = "123456789"
    b = '<h1>123456</h1>'
    c = EmailMultiAlternatives(title,a,email_from,resc)
    c.attach_alternative(b,'text/html')
    c.send()
    return HttpResponse('ok')


