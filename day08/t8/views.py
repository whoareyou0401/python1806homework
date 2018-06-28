from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail,send_mass_mail,EmailMultiAlternatives
# Create your views here.
def send_my_mail(req):
    title = "啧啧"
    message = "你是大傻逼......"
    email_from = "1846818768@qq.com"
    recs = ["1846818768@qq.com","1947380879@qq.com"]
    send_mail(title,message,email_from,recs)
    return HttpResponse("嗨起来")

# def send_emailess(req):
#     title1 = "阿里11111111阿里"
#     message = "恭喜111111111111你成为.............."
#     email_from = "1846818768@qq.com"
#     title2 = "阿里2222222222阿里"
#     message = "恭喜22222222222你成为.............."
#     email_from = "1846818768@qq.com"

def email_html(req):
    title4 = "大白兔白又白，"
    message = "儿子我是你爸爸......"
    email_from = "1846818768@qq.com"
    recs = ["1846818768@qq.com", "1947380879@qq.com"]
    html_content = '<p><a href = "http://47.96.119.211:18468/html">美女姐姐快点我</a></p>'
    msg = EmailMultiAlternatives(title4,message,email_from,recs)
    msg.attach_alternative(html_content,"text/html")
    msg.send()
    return HttpResponse("哈喽，傻屌霞")


