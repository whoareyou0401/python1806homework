from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from t8 import my_util
from django.core.cache import cache


# Create your views here.
#单个发送
def my_send_mail(req):
    title = "这个是测试"
    message = "应该是能接收到的吧"
    email_from = "18342213583@163.com"
    receive = ["18342213583@163.com"]
    send_mail(title, message, email_from, receive)
    return HttpResponse("ok")
#群发
def send_mail_ss(req):
    title = "假的假的"
    message1 = "咦咦咦咦咦咦咦"
    emailfrom = "18342213583@163.com"
    title2 = "来自外星的邮件"
    message2 = "来自Djanggo的邮件"
    # rec1 = ["17694871425@163.com",
    #         "569677884@ qq.com",
    #         "liuda@1000phone.com"]
    # rec2 = ["17694871425@163.com",
    #         "569677884@qq.com"]
    rec1 = ["13663641298@163.com"]
    rec2 = ["13663641298@163.com"]
    senders1 = (title, message1 ,emailfrom, rec1)
    senders2 = (title2, message2, emailfrom, rec2)
    send_mass_mail((senders1, senders2), fail_silently=False)
    return HttpResponse("ok")

#发送html页面

def send_email_html(req):
    title = "这个是测试"
    message = "应该是能接收到的吧"
    email_from = "18342213583@163.com"
    receive = ["18342213583@163.com",
               "569677884@qq.com"
               ]
    htmlcontent = '<p>This is an <strong>important</strong> message.<strong>I Love You<img src="https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=431792944,1008990118&fm=200&gp=0.jpg"></strong></p>'
    msg = EmailMultiAlternatives(title, message, email_from, receive)
    msg.attach_alternative(htmlcontent, "text/html")
    msg.send()
    return HttpResponse("发送完成")

def get_verify_code(req):
    param = req.GET
    email = param.get('email')
    name = param.get('name')
    token = my_util.get_token()
    verify_url = "http://192.168.11.133:8000/verify/" + token
    cache.set(token, email, 70)

    title = "欢迎注册我的天啊会员"
    message = "请点击下面链接进行验证{url}".format( url = verify_url )
    email_from = "18342213583@163.com"
    send_mail(title, message, email_from, [email])
    return HttpResponse("发送成功,请查看邮箱进行验证。")

def verify(req, token):
    email = cache.get(token)
    if email:
        return HttpResponse("验证成功，这是假的,接下来应该是修改用户的状态")
    else:
        return HttpResponse("验证链接不正确")