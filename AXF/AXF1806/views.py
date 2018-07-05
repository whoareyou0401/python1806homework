from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View
from .axf_utils import send_active_email

from AXF1806 import models
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
        "title": title,
        'swipers': swipers,
        'mynavs': navs,
        'mustbuys': mustbuys,
        'shop0': shop0,
        'shop1_3': shops[1:3],
        'shop3_7': shops[3:7],
        'shop7_11': shops[7:],
        'maininfos': maininfos
    }
    return render(req, 'home/home.html', context=data)


def market(req):

    # 做重定向
    return redirect(reverse('axf:market_with_param', args=('104749', '0', "0")))


def market_with_param(req, param_typeid, sub_typeid, sort_type):
    sort_type = int(sort_type)
    g_types = models.GoodsTypes.objects.all()
    if int(sub_typeid) == 0:
        goods = models.Goods.objects.filter(categoryid=param_typeid)
    else:
        goods = models.Goods.objects.filter(categoryid=param_typeid, childcid=sub_typeid)

    ZH_SORT = 0
    PRICE_SROT = 1
    SALE_SORT = 2
    if sort_type == ZH_SORT:
        pass
    elif sort_type == PRICE_SROT:
        goods = goods.order_by('price')
    else:
        goods = goods.order_by('productnum')
    print(goods)

    sub_cates = g_types.filter(typeid=param_typeid)
    my_sub_types = []
    if sub_cates.count() <= 0:
        raise Exception("nothing find")
    else:
        # 根据类型id拿到子类id
        sub_cates_str = sub_cates.first().childtypenames
        # 对数据进行切分处理
        sub_cates_array = sub_cates_str.split('#')
        print(sub_cates_array)
        for i in sub_cates_array:
            tmp = i.split(':')
            my_sub_types.append(tmp)
        # print(my_sub_types)


    data ={
        'title': '闪购',
        'goodstypes': g_types,
        'selectedid': param_typeid,
        'goods': goods,
        'sub_types': my_sub_types,
        'selectedid_sub_type_id': sub_typeid,
        'sort_type': int(sort_type)

    }
    return render(req, 'market/market.html', data)


def cart(req):
    return render(req, 'cart/cart.html')


def mine(req):
    return render(req, 'mine/mine.html')


class RegisterAPI(View):

    def get(self, req):
        return render(req, 'user/register.html')

    def post(self, req):
        # //校验用户名是不是规则
        # //邮箱是否合法
        # //密码长度和规则 正则可以实现

        # 拿参数
        params = req.POST
        u_name = params.get('u_name')
        pwd = params.get('pwd')
        pwd_confirm = params.get('pwd_confirm')
        email = params.get('email')

        # 校验邮箱的合法性 正则可以实现

        # 拿图片
        icon = req.FILES.get('icon')
        # 用户的简单校验
        user_count = models.MyUser.objects.filter(username=u_name).count()
        if user_count != 0:
            return HttpResponse('该用户已存在')

        if pwd and pwd_confirm and pwd == pwd_confirm:
            # 新建用户
            user = models.MyUser.objects.create_user(
                username=u_name,
                email=email,
                password=pwd,
                icon=icon,
                is_active=False
            )
            send_active_email(email)
            return redirect(reverse('axf:login'))
        else:
            return HttpResponse('shibai')

class LoginApi(View):
    def get(self, req):
        return render(
            req, 'user/login.html'
        )


def active(req, token):
    email = cache.get(token)
    if email:
        user = models.MyUser.objects.filter(email=email)
        if user.count() == 1:
            user.is_active = True
            return redirect(reverse('axf:mine'))
        else:
            return HttpResponse("<h1>密码失效</h1>")
    else:
        return HttpResponse("<h1>密码失效，请重新注册</h1>")









