from django.http import HttpResponse
from django.shortcuts import render
from ashuang.models import *
# from django.http import HttpResponse

# Create your views here.


def test(req):
    return render(req, 'test.html')


def cate_view(req):
    # cates = Categary.objects.filter(name='饮料')
    cates = Categary.objects.all()
    return render(req, 'test.html', context={'cates': cates})

# def cate_view(req):
#     cates=Categary.objects.all()
#     return render(req,"text.html",context={"cates":cates})

def item_view(req):
    print(req.GET)
    cate_id = req.GET.get("cate_id")
    items=Item.objects.all()
    items=items.filter(categary_id=cate_id)
    return render(req,"items.html",{"items":items})


def item_view(req):
    print(req.GET)
    # cate_id = req.GET.get("cate_id ")
    cate_id = req.GET.get("cate_id")
    items = Item.objects.all()
    items = items.filter(categary_id=cate_id)
    return render(req, "items.html", {"items": items})


def get_item(req):
    # item_id = req.GET.get('item_id')
    item_id = req.GET.get("item_id")
    my_item = Item.objects.get(pk=int(item_id))
    return HttpResponse(my_item.name)
