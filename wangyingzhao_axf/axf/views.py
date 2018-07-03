from django.shortcuts import render, redirect
from axf import models
# Create your views here.
from django.urls import reverse


def home(req):
    title = "首页"
    swipers = models.Wheel.objects.all()
    mynavs = models.Nav.objects.all()
    mustbuys = models.MustBuy.objects.all()
    shops = models.axf_shop.objects.all()
    shop0 = shops[0]
    shop1_3 = shops[1:3],
    shop3_7 = shops[3:7]
    shop7_11 = shops[7:11]
    maininfos = models.HomeMainShow.objects.all()
    data = {
        'title': title,
        'swipers': swipers,
        'mynavs':mynavs,
        'mustbuys':mustbuys,
        'shop0':shop0,
        'shop1_3':shop1_3,
        'shop3_7': shop3_7,
        'shop7_11': shop7_11,
        'maininfos':maininfos,

    }
    return render(req, 'home/home.html',context=data)

def market(req):
    # g_types = models.GoodsTypes.objects.all()
    # data = {
    #     'title':'闪购',
    #     'goodstypes':g_types,
    # }
    # return render(req,'market/market.html',data)
    return redirect(reverse("axf:market_with_param",args=(104749,)))

def market_with_param(req, typeid):
    g_types = models.GoodsTypes.objects.all()
    # typeid从前端传过来后变成字符串了。
    typeid = int(typeid)
    goods = models.Goods.objects.filter(categoryid=typeid)
    print(goods)
    data = {
        'title': '闪购',
        'goodstypes': g_types,
        'selecteid': typeid,
        'goods':goods,
    }
    return render(req, 'market/market.html', data)

def cart(req):
    return render(req, 'cart/cart.html')

def mine(req):
    return render(req, 'mine/mine.html')