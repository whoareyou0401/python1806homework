from django.http import HttpResponse
from django.shortcuts import render
from .tasks import hello_celery,get_data_with_param
# Create your views here.
from .models import MyData
import time
from .my_singals import action
from django.views.generic import View


def index(req):
    loop = 3
    get_data_with_param.delay(loop)
    return HttpResponse("欢迎光临")

def test_singal(request):
    # obj = MyData()
    # obj.data = "呵呵"
    # obj.save()
    action.send(sender="dada",data="hehe")
    return HttpResponse("ok")

class MyDataAPI(View):
    def get(self,requese):
        print("别调用")
        print(requese.GET.get('id'))
        return HttpResponse("ok")

    def ppst(self,requese):
        print(requese.POST.get("id"))
        return HttpResponse("POST响应")
    def delete(self,requese):
        print(requese.body)
        return HttpResponse("delate响应")

def get_restful(req):
    return render(req,"restful.html")