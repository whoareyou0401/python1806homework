from django.shortcuts import render
from axf import models
# Create your views here.

def home(req):
    title = "首页"
    swipers = models.Wheel.objects.all()
    data = {
        'title': title,
        'swipers': swipers
    }
    return render(req, 'home/home.html', context=data)

def market(req):
    return render(req, 'market/market.html')

def cart(req):
    return render(req, 'cart/cart.html')

def mine(req):
    return render(req, 'mine/mine.html')