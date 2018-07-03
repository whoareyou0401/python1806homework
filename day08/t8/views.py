from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, send_mass_mail,EmailMultiAlternatives
import logging

# Create your views here.

def send_my_mail(req):
    title = "阿里offer"
    message = "恭喜您，成为我们的一员"
    email_from = "648328530@qq.com"
    recs = ["jinguangzhu522@163.com"]
    send_mail(title,message,email_from,recs)
    return HttpResponse("发送成功")

def send_emailss(req):
    title1 = "tencentoffer"
    message1 = "恭喜您，被骗了"
    email_from = "648328530@qq.com"
    title2 = "这是一封找事情的邮件"
    message2 = "大大大大大哥别杀我"
    recs1 = ["jinguangzhu522@163.com"]
    recs2 = ["jinguangzhu522@163.com","jinguangzhu523@163.com"]
    sender1 = (title1, message1, email_from, recs1)
    sender2 = (title2, message2, email_from, recs2)
    send_mass_mail((sender1,sender2),fail_silently=False)
    return HttpResponse("OK")

def email_html(req):
    title = "阿里offer"
    message = "恭喜您，成为我们的一员"
    email_from = "648328530@qq.com"
    recs = ["jinguangzhu522@163.com"]
    html_content = '<p>This is an <strong>重要文件</strong> message.</p>'
    msg = EmailMultiAlternatives(title,message,email_from,recs)
    msg.attach_alternative(html_content,"text/html")
    msg.send()
    return HttpResponse("ook")


def test_log(req):
    logger = logging.getLogger("django")
    logger.warning("this is warning python1806")
    return HttpResponse("ok")