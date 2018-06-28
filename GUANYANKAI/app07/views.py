from django.shortcuts import render
import time
from django.http import HttpResponse
from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
from django.views.decorators.cache import cache_page


# @cache_page(60)
def my_data(req):
    # time.sleep(4)
    # return HttpResponse('ok')

    # cache.set()
    data = cache.get("val")
    if data:
        return HttpResponse(str(data))
    else:
        time.sleep(4)
        cache.set('val','hehe',30)
        return HttpResponse('hehe')

def get_rtf(req):
    return render(req,"RTF.html")