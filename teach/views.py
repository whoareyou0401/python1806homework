from django.http import HttpResponse
from django.shortcuts import render
from teach.models import *

# Create your views here.
def test(req):
    return  render(req, "test.html")

def cate_view(req):
    # cates = Categary.objects.filter(name="饮料")
    cates = Categary.objects.all()
    return render(req, "test.html", context={"cates": cates})

def item_view(req):
    print(req.GET)
    cate_id = req.GET.get("cate_id")
    items = Item.objects.all()
    items = items.filter(categary_id=cate_id)
    return render(req, "items.html", {"items": items})

def get_item(req):
    item_id = req.GET.get("item_id")
    try:
        my_item = Item.objects.get(pk=int(item_id))
    except Item.DoesNotExist:
        return HttpResponse("没有啦")
    return HttpResponse(my_item.name)

def search_item_by_price(req):
    # name = req.GET.get("i_name")
    price = req.GET.get("price")
    items = Item.objects.filter(price__in=[price, 20])
    return render(req, "items.html", {"items": items})

def search_item_by_name(req):
    name = req.GET.get("i_name")
    print(name)
    # price = req.GET.get("price")
    items = Item.objects.filter(name__startswith=name)
    print(items)
    return render(req, "items.html", {"items": items})

def search_item_by_time(req):
    my_time = req.GET.get("t")
    items = Item.objects.filter(come_in_time__year=my_time)
    return render(req, "items.html", {"items": items})