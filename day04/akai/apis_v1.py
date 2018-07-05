from django.db.models import F, Q
from django.forms import model_to_dict
from django.http import HttpResponse
from akai.models import *


def add_language_api(req):
    param = req.POST
    name = param.get('name','python')
    desc = param.get('desc', '人生苦短，我用python')
    c = ComLanguage.objects.create(name=name, desc=desc)
    return HttpResponse('您已经成功创建{l}'.format(l=name))
