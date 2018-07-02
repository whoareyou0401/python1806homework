import hashlib

from django.db import models


class Home(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField(default=1)

    class Meta:
        abstract = True


class HomeWheel(Home):
    class Meta:
        db_table = 'axf_wheel'


class HomeNav(Home):
    class Meta:
        db_table = 'axf_nav'


class HomeMustBuy(Home):
    class Meta:
        db_table = 'axf_mustbuy'


class HomeShop(Home):
    class Meta:
        db_table = 'axf_shop'


"""
(trackid,name,img,categoryid,brandname,img1,childcid1,productid1,longname1,price1,marketprice1,
img2,childcid2,productid2,longname2,price2,marketprice2,img3,childcid3,productid3,longname3,price3,marketprice3)
"""


class HomeMainShow(Home):
    categoryid = models.IntegerField(default=1, verbose_name='分类id')

    brandname = models.CharField(max_length=32, verbose_name='类名字')

    img1 = models.CharField(max_length=200)

    childcid1 = models.IntegerField(default=1)

    productid1 = models.IntegerField(default=1)

    longname1 = models.CharField(max_length=128)

    price1 = models.FloatField(default=0)

    marketprice1 = models.FloatField(default=0)

    img2 = models.CharField(max_length=200)

    childcid2 = models.IntegerField(default=1)

    productid2 = models.IntegerField(default=1)

    longname2 = models.CharField(max_length=128)

    price2 = models.FloatField(default=0)

    marketprice2 = models.FloatField(default=0)

    img3 = models.CharField(max_length=200)

    childcid3 = models.IntegerField(default=1)

    productid3 = models.IntegerField(default=1)

    longname3 = models.CharField(max_length=128)

    price3 = models.FloatField(default=0)

    marketprice3 = models.FloatField(default=0)

    class Meta:
        db_table = 'axf_mainshow'


"""
typeid,typename,childtypenames,typesort
"""


class Foodtype(models.Model):
    typeid = models.IntegerField(default=1)
    typename = models.CharField(max_length=16)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_foodtypes'


"""
(productid,productimg,productname,productlongname,isxf,pmdesc,specifics,price,marketprice,categoryid,childcid,
childcidname,dealerid,storenums,productnum) values("11951","http://img01.bqstatic.com/upload/goods/000/001/1951/0000011951_63930.jpg@200w_200h_90Q",
"","乐吧薯片鲜虾味50.0g",0,0,"50g",2.00,2.500000,103541,103543,"膨化食品","4858",200,4)
"""


class Goods(models.Model):
    productid = models.IntegerField(default=1)
    productimg = models.CharField(max_length=256)
    productname = models.CharField(max_length=128)
    productlongname = models.CharField(max_length=256)
    isxf = models.BooleanField(default=False)
    pmdesc = models.BooleanField(default=False)
    specifics = models.CharField(max_length=32)
    price = models.FloatField(default=1)
    marketprice = models.FloatField(default=2)
    categoryid = models.IntegerField(default=1)
    childcid = models.IntegerField(default=1)
    childcidname = models.CharField(max_length=128)
    dealerid = models.IntegerField(default=1)
    storenums = models.IntegerField(default=2)
    productnum = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_goods'


class UserModel(models.Model):
    u_name = models.CharField(max_length=16, unique=True)
    u_password = models.CharField(max_length=128)
    u_email = models.CharField(max_length=64, unique=True)
    u_icon = models.ImageField(upload_to='icons')
    is_delete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


    # 设置密码
    def set_password(self, password):

        self.u_password = self.generate_hash(password)

    # 对密码进行哈希算法
    def generate_hash(self, password):

        sha = hashlib.sha512()
        sha.update(password.encode('utf-8'))

        return sha.hexdigest()

    # 检验密码是否一致
    def check_password(self, password):
        return self.u_password == self.generate_hash(password)

    class Meta:
        db_table = 'axf_user'


class CartModel(models.Model):
    c_goods_num = models.IntegerField(default=1)
    c_goods_select = models.BooleanField(default=True)
    c_goods = models.ForeignKey(Goods)
    c_user = models.ForeignKey(UserModel)

    class Meta:
        db_table = 'axf_cart'


class OrderModel(models.Model):

    o_user = models.ForeignKey(UserModel)

    """
        0 已下单，未付款
        1 已下单，已付款，未发货
        2 已下单，已付款，已发货，未收货
        3 已下单，xxxxxx
    
    """
    o_status = models.IntegerField(default=0)

    o_time = models.DateTimeField(auto_now=True)

    o_price = models.FloatField(default=0)

    class Meta:
        db_table = 'axf_order'


class OrderGoods(models.Model):

    o_order = models.ForeignKey(OrderModel)

    o_goods = models.ForeignKey(Goods)

    o_goods_num = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_ordergoods'