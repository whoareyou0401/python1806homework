import time
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page


# @cache_page(60)
def my_data(req):
    # time.sleep(4)
    # return HttpResponse('0k')

    date = cache.get('val')
    if date:
        return HttpResponse(str(date))
    else:
        time.sleep(4)
        cache.set("val",'heh',30)
        return HttpResponse('hehe')
