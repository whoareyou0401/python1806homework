import time

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page


@cache_page(60)
def ma_data(req):
    time.sleep(5)
    return HttpResponse("ok")

