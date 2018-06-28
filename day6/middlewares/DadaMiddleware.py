from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class LearnMiddleware(MiddlewareMixin):
    def process_request(self, req):
        ip = req.META.get("REMOTE_ADDR")
        print(ip)
        # balcks = ['111.206.170.62'] # 黑名单
        # if ip in balcks:
        #     return HttpResponse("小伙子 缺媳妇吗")
        name = req.POST.get("u_name")
        if name == 'akai':
            return HttpResponse("获得特等奖 智能媳妇一枚，上得了厅堂，下得了厨房。奖大赠小，一天就能实现当爹梦想")

