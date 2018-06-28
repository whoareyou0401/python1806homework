from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail,send_mass_mail,EmailMultiAlternatives
# Create your views here.

def send_my_mail(req):
    title = '阿里offer'
    message = '恭喜恭喜'
    email_from = '69189668@qq.com'
    resc = ['13383332752@163.com']
    send_mail(title,message,email_from,resc)
    return HttpResponse('CEO开始嗨起来')

def send_mass_email(req):
    title1 = '腾讯offer'
    message1 = '恭喜 别骗'
    email_from = '69189668@qq.com'

    title2 = '这是一封挑事的邮件'
    message2 = '大哥别杀我'
    resc1 = ['13383332752@163.com']
    resc2 = ['13383332752@163.com']

    senders1 = (title1,message1,email_from,resc1)
    senders2 = (title2,message2,email_from,resc2)
    send_mass_mail((senders1,senders2),fail_silently=False)
    return HttpResponse('ok')

def email_html(req):
    title = '阿里offer'
    message = '恭喜恭喜'
    email_from = '69189668@qq.com'
    resc3 = ['13383332752@163.com']

    html_con = '<a href={url}>{url}</a>'.format(url=url)
    msg = EmailMultiAlternatives(title,message,email_from,resc3)
    msg.attach_alternative(html_con,"text/html")
    msg.send()
    return HttpResponse('ok')

# 邮箱验证码





