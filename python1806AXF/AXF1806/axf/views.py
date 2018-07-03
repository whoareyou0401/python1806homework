from django.shortcuts import render, redirect
from django.urls import reverse

from axf import models
# Create your views here.

def home(req):
    title = "首页"
    swipers = models.Wheel.objects.all()
    navs = models.Nav.objects.all()
    mustbuys = models.MustBuy.objects.all()
    shops = models.Shop.objects.all()
    maininfos = models.MainInfo.objects.all()
    shop0 = shops[0]

    data = {
        'title':title,
        'swipers':swipers,
        'mynavs':navs,
        'mustbuys':mustbuys,
        'shop0':shop0,
        'shop1_3':shops[1:3],
        'shop3_7' : shops[3:7],
        'shop7_11': shops[7:],
        'maininfos':maininfos,
    }

    return render(req,'home/home.html',context=data)

def market(req):
    # g_types = models.GoodsTypes.objects.all()
    # data = {
    #     'title':"闪购",
    #     'goodstypes':g_types,
    # }
    return redirect(reverse("axf:market_with_param",args=("104749",)))

def market_with_param(req,typeid):
    g_types = models.GoodsTypes.objects.all()
    goods = models.Goods.objects.filter(categoryid=typeid)
    data = {
        'title': "闪购",
        'goodstypes': g_types,
        'selectedid':typeid,
        'goods':goods
    }
    return render(req, 'market/market.html',data)

def cart(req):
    return render(req, 'cart/cart.html')

def mine(req):
    return render(req, 'mine/mine.html')





