import time

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page


@cache_page(60)
def my_data(req):
    cache.set()
    data = cache.get("val")
    if data:
        return HttpResponse(str(data))
    else:
        # 假装在拼命的拿数据
        time.sleep(4)
        # 拿到数据后
        cache.set("val", "hehe", "30")
        return HttpResponse("hehe")
def get_rtf(req):
    return render(req, "RTF.html")