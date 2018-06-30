from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from .tasks import get_data,get_data_with_param
from .models import MyData
from .my_singals import action
from  django.views.generic import View

import time
# Create your views here.
# def get_data():
#     time.sleep(3)


def index(req):
    loop=3
    get_data_with_param.delay(loop)
    return HttpResponse("欢迎光临")

def test_singal(request):
    # obj = MyData()
    # obj.data = "hehe"
    # obj.save()
    action.send(sender="dada",data="hehe")
    return HttpResponse("ok")
class MyDataAPI(View):
    def get(self,request):
        print("被调用")
        print(request.GET.get('id'))
        return HttpResponse("ok")
    def post(self,request):
        print(request.POST.get("id"))
        return HttpResponse("post相应")
    def delete(self,request):
        print(request.body)
        print(QueryDict(request.body))
        return HttpResponse("delect相应")

def get_restful(req):
    return render(req,"restful.html")