import uuid

import hashlib
import os

import random
from django.http import HttpResponse
from django.shortcuts import render
from t6.models import Stu
# Create your views here.
from django.conf import settings


def hello(req):
    return HttpResponse("你好" + req.META["REMOTE_ADDR"])


def luck(req):
    if req.method == "GET":
        return render(req,"yaojiang.html")
    else:
        param = req.POST
        name=param.get('u_name')
        res = random.randint(0, 100)
        if res > 90:
            return HttpResponse('恭喜' + name + '获得一等奖')
        else:
            return HttpResponse('获得酱油一瓶')


def get_filename():
    my_uuid = uuid.uuid4()
    uuid_str = str(my_uuid).encode("utf-8")
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()


def userinfo(req):
    if req.method == "GET":
        return render(req, "userinfo.html")
    else:
        s_name = req.POST.get("s_name")
        icon = req.FILES["icon"]
        # print(s_name)
        # print(icon)
        Stu.objects.create(s_name=s_name, icon=icon)
        filename = get_filename()
        filepath = os.path.join(settings.MEDIA_ROOT, '{f_name}.jpg'.format(f_name=filename))
        print(icon.name)
        #打开我们自己的hehe.jpg
        with open(filepath,'wb') as imgfile:
            #将图片数据切分成小块icon.chunks()
            for data in icon.chunks():
                #遍历切分完的数据，写入hehe.jpg
                imgfile.write(data)
                #冲刷缓存区
                imgfile.flush()
        #     # imgfile.save()
        return HttpResponse("ok")

