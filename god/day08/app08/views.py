import uuid

import hashlib
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives


# Create your views here.



def send_my_mail(req):
    title = "offer"
    message = "恭喜您 啦啦啦"
    email_from = "18633383217@163.com"
    recs = ["840111882@qq.com",]
    send_mail(title,message,email_from,recs)
    return HttpResponse("啦啦啦")

def send_emails(req):
    title = "offer"
    message = "恭喜您 啦啦啦"
    email_from = "18633383217@163.com"
    title2 = "查水表"
    message2 = "是 他 是 他 就 是 他"
    title3 = "啦啦啦德玛西亚"
    message3 = "蒸羊羔、蒸熊掌、蒸鹿尾儿、烧花鸭、烧雏鸡、烧子鹅，卤猪、卤鸭、酱鸡、腊肉、松花、小肚儿、晾肉、香肠儿，什锦苏盘儿、熏鸡白肚儿、清蒸八宝猪、江米酿鸭子，罐儿野鸡、罐儿鹌鹑、卤什件儿、卤子鹅、山鸡、兔脯、菜蟒、银鱼、清蒸哈士蟆！烩腰丝、烩鸭腰、烩鸭条、清拌鸭丝儿、黄心管儿，焖白鳝、焖黄鳝、豆豉鲶鱼、锅烧鲤鱼、锅烧鲶鱼、清蒸甲鱼、抓炒鲤鱼、抓炒对虾、软炸里脊、软炸鸡！什锦套肠儿、麻酥油卷儿、卤煮寒鸦儿，熘鲜蘑、熘鱼脯、熘鱼肚、熘鱼骨、熘鱼片儿、醋熘肉片儿！烩三鲜儿、烩白蘑、烩全饤儿、烩鸽子蛋、炒虾仁儿、烩虾仁儿、烩腰花儿、烩海参、炒蹄筋儿、锅烧海参、锅烧白菜、炸开耳、炒田鸡，还有桂花翅子、清蒸翅子、炒飞禽、炸什件儿、清蒸江瑶柱、糖熘芡实米，拌鸡丝、拌肚丝、什锦豆腐、什锦丁儿，糟鸭、糟蟹、糟鱼、糟熘鱼片、熘蟹肉、炒蟹肉、清拌蟹肉，蒸南瓜、酿倭瓜、炒丝瓜、酿冬瓜、焖鸡掌儿、焖鸭掌儿、焖笋、烩茭白，茄干晒炉肉、鸭羹、蟹肉羹、三鲜木樨汤！还有红丸子、白丸子、熘丸子、炸丸子、南煎丸子、苜蓿丸子、三鲜丸子、四喜丸子、鲜虾丸子、鱼脯丸子、饹炸丸子、豆腐丸子、氽丸子！一品肉、樱桃肉、马牙肉、红焖肉、黄焖肉、坛子肉、烀肉、扣肉、松肉、罐儿肉、烧肉、烤肉、大肉、白肉、酱豆腐肉！红肘子、白肘子、水晶肘子、蜜蜡肘子、酱豆腐肘子、扒肘子！炖羊肉、烧羊肉、烤羊肉、煨羊肉、涮羊肉、五香羊肉、爆羊肉，氽三样儿、爆三样儿、烩银丝、烩散丹、熘白杂碎、三鲜鱼翅、栗子鸡、煎氽活鲤鱼、板鸭、筒子鸡！烩长脐肚、烩南荠、盐水肘花儿、锅烧猪蹄儿！拌稂子、炖吊子、烧肝尖儿、烧连贴、烧肥肠儿、烧宝盖儿、烧心、烧肺、油炸肺，酱蘑饤、龙须菜、拌海蜇、玉兰片、糖熘饹炸、糖腌饯莲子、拔丝山药、拔丝肉，鳎目鱼、八代鱼、黄花鱼、海鲫鱼、鲥鱼、鲑鱼，扒海参、扒燕窝、扒鸡腿儿、扒鸡块儿、扒鱼、扒肉、扒面筋、扒三样儿，红肉锅子、白肉锅子、什锦锅子、一品锅子、菊花锅子"
    recs = ["840111882@qq.com", "619469958@qq.com"]
    senders1 = (title, message, email_from, recs)
    senders2 = (title2,message2,email_from,recs)
    senders3 = (title3,message3,email_from,recs)
    send_mass_mail((senders1,senders2,senders3),
                   fail_silently=False
                   )
    return HttpResponse("ok")


def email_html(req):
    title = "今日头条"
    message = "针对近期房地产市场乱象，为严厉打击侵害群众利益的违法违规行为，住房城乡建设部会同其他六部委联合印发了《关于在部分城市先行开展打击侵害群众利益违法违规行为 治理房地产市场乱象专项行动的通知》，决定于2018年7月初至12月底，在北京、上海等30个城市先行开展治理房地产市场乱象专项行动。此次行动，将重点打击投机炒房行为和房地产“黑中介”"
    email_from = "18633383217@163.com"
    recs = ["840111882@qq.com", ]
    send_mail(title, message, email_from, recs)
    html_content = '<p>aaaa<strong>asfds</strong>asd<h1>as</h1></p>'
    msg = EmailMultiAlternatives(title, message, email_from, recs)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return HttpResponse("啦啦啦")


def get_token():
    u_token = uuid.uuid4()
    u_str = str(u_token).encode("utf-8")

    md5 = hashlib.md5()
    md5.update(u_str)
    return md5.hexdigest()

def register_email(req):
    if req.method == "GET":
        return render(req,"register_email.html")
    else:
        param =req.POST
        name = param.get("u_name")
        email = param.get("u_email")
        token = get_token()
        verify_url = "http://heyidan.cn:12348/register/" + token
        cache.set(token,email,60)


        title = "欢迎注册1806"
        message = "请将链接复制到浏览器完成验证{url}".format(
            url = verify_url
        )
        email_from = "18633383217@163.com"
        send_mail(title,message,email_from,[email])
        return HttpResponse("注册成功，请登录邮箱进行激活")

def verify(req,token):
    email = cache.get(token)
    if email:
        return HttpResponse("ok")
    else:
        return HttpResponse("验证链接不正确")

