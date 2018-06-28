from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class LearnMiddleware(MiddlewareMixin):
    def process_request(self, req):
        ip = req.META.get("REMOTE_ADDR")
        print(ip)
        balcks = ['114.242.26.144']
        if ip in balcks:
            return HttpResponse("小伙子 爬虫不是那么好干的")
        name = req.POST.get("u_name")
        if name=='dada':
            return HttpResponse("获得特等价 特斯拉一辆")

