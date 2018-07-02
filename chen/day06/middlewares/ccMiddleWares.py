from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


# class LearnMiddleware(MiddlewareMixin):
#     def process_request(self,req):
#         ip = req.META.get('REMOTE_ADDR')
#         # blocks = ['114.242.26.54']
#         # print(ip)
#         # if ip in blocks:
#         #     return HttpResponse("小伙子爬虫不是那么好干得")