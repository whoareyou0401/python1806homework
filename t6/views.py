import random
from django.http import HttpResponse
from django.shortcuts import render
from t6.models import Stu
from  django.conf import settings
import os
# from t6.t6_utils import get filename

# Create your views here.

def hello(req):
    return HttpResponse("你好"+req.META["REMOTE_ADDR"])

def luck(req):
    if req.method == "GET":
        return render(req,'yaojiang.html')
    else:
        param = req.POST
        name = param.get("u_name")
        res = random.randint(0,100)
        if res > 90:
            return HttpResponse("恭喜" + name + "获得一百元")
        else:
            return HttpResponse("很抱歉，没有中奖")

def userinfo(req):
    if req.method == "GET":
        return render(req,"userinfo.html")
    else:
        s_name = req.POST.get("s_name")
        icon = req.FILES["icon"]
        # print(s_name)
        # print(icon)
        # Stu.objects.create(s_name=s_name,icon=icon)

        # 第二张方法
        filepath = os.path.join(settings.MEDIA_ROOT,'icons/hehe.jpg')
        print(icon.name)
        with open(filepath,'wb') as imgfile:
            for data in icon.chunks():
                imgfile.write(data)
                imgfile.flush()

        return HttpResponse("ok")

