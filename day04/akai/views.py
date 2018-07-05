from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from django.template import loader
# Create your views here.



def language_view(req):
    # load.get_te
    return render(req, 'add-language.html')


def language_v2_view(req):
    temp = loader.get_template('add-language.html')
    # print(temp)
    # print(dir(temp))
    # 渲染
    res = temp.render()
    return HttpResponse(res)

def get_langs_view(req):
    res = ComLanguage.objects.all()
    return render(req, 'langes.html',{'langs': res})



