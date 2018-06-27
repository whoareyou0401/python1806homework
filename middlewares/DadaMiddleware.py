from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class LearnMiddleware(MiddlewareMixin):
    def process_request(self,req):
        ip = req.META.get('REMOTE_ADDR')
        print(ip)
        black = ['111.22.123.43']
        if ip in black:
            return HttpResponse("放弃吧，朋友")
        name = req.POST.get('u_name')
        if name =="小明":
            return HttpResponse("滚出去！！")
