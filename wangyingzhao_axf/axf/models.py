from django.db import models

# Create your models here.
class BaseData(models.Model):
    img = models.CharField(
        max_length=255,
        verbose_name="图片链接"
    )
    name = models.CharField(
        max_length=100,
        verbose_name='介绍名字'
    )
    trackid =models.CharField(
        max_length=100,
        verbose_name='trackid'
    )
    class Meta:
        abstract = True

class Wheel(BaseData):
    class Meta:
        db_table="axf_wheel"

class Nav(BaseData):
    class Meta:
        db_table="axf_nav"

class MustBuy(BaseData):
    class Meta:
        db_table="axf_mustbuy"

class axf_shop(BaseData):
    class Meta:
        db_table="axf_shop"


class HomeMainShow(BaseData):
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

'''
typeid,typename,childtypenames,typesort
'''
class GoodsTypes(models.Model):
    typeid = models.IntegerField(
        default=1
    )
    typename = models.CharField(
        max_length=16
    )
    childtypenames = models.CharField(
        max_length=200
    )
    typesort = models.IntegerField(
        default=1
    )

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

