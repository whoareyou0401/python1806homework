from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, send_mass_mail,EmailMultiAlternatives
# Create your views here.
import logging
def send_my_mail(req):
    title = "阿里offer"
    message = "恭喜您 成为我们公司的CEO"
    email_from = "3369571193@qq.com"
    recs = ["1486412190@qq.com","ichenyouzhi@163.com","1439854134@qq.com"]
    send_mail(title,message,email_from,recs)
    return HttpResponse("小姐姐打的")
#
#
def send_emailss(req):
    title1 = "腾讯offer"
    message1 = "恭喜你 被骗了"
    email_from = "3369571193@qq.com"
    title2 = "一封挑事邮件"
    message2 = "大哥大哥"
    resc1 =[
        "1486412190@qq.com", "ichenyouzhi@163.com"
    ]
    resc2 = ["1486412190@qq.com","ichenyouzhi@163.com"
             "m18742863100@163.com","1439854134@qq.com"]
    senders1 = (title1,message1,email_from,resc1)
    senders2 = (title2,message2,email_from,resc2)
    send_mass_mail((senders1,senders2),fail_silently=False)
    return HttpResponse("ok")

def email_html(req):
    title = "阿里offer"
    message = "恭喜您 成为我们公司的CEO"
    email_from = "3369571193@qq.com"
    recs = ["1486412190@qq.com","ichenyouzhi@163.com","1439854134@qq.com"]
    html_content = '<p>This is an <strong>bbbbbbb</strong> message.</p>'
    msg = EmailMultiAlternatives(title,message,email_from,recs)
    msg.attach_alternative(html_content,"text/html")
    msg.send()
    return HttpResponse("ok了")

# def test_log(req):
#     logger = logging.getLogger('django')
#     logger.warning("thi is python 1906")
#     return HttpResponse("ok")