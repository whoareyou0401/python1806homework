from django.db import models

# Create your models here.
class BaseData(models.Model):
    img = models.CharField(
        max_length=255,
        verbose_name="图片连接"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="介绍名字"
    )
    trackid = models.CharField(
        max_length=100,
        verbose_name="trackid"
    )
    class Meta:
        #抽象类
        abstract = True

class Wheel(BaseData):
        #换表名
    class Meta:
        db_table="axf_wheel"

class Nav(BaseData):

    class Meta:
        db_table="axf_nav"

class MustBuy(BaseData):

    class Meta:
        db_table="axf_mustbuy"

class Shop(BaseData):

    class Meta:
        db_table="axf_shop"



class MainInfo(models.Model):
    trackid = models.CharField(
        max_length=200
    )
    name = models.CharField(
        max_length=200
    )
    img = models.CharField(
        max_length=200
    )
    categoryid = models.CharField(
        max_length=200
    )
    brandname = models.CharField(
        max_length=200
    )
    img1 = models.CharField(
        max_length=200
    )
    childcid1 = models.CharField(
        max_length=200
    )
    productid1 = models.CharField(
        max_length=200
    )
    longname1 = models.CharField(
        max_length=200
    )
    price1 = models.CharField(
        max_length=200
    )
    marketprice1 = models.CharField(
        max_length=200
    )
    img2 = models.CharField(
        max_length=200
    )
    childcid2 = models.CharField(
        max_length=200
    )
    productid2 = models.CharField(
        max_length=200
    )
    longname2 = models.CharField(
        max_length=200
    )
    price2 = models.CharField(
        max_length=200
    )
    marketprice2 = models.CharField(
        max_length=200
    )
    img3 = models.CharField(
        max_length=200
    )
    childcid3 = models.CharField(
        max_length=200
    )
    productid3 = models.CharField(
        max_length=200
    )
    longname3 = models.CharField(
        max_length=200
    )
    price3 = models.CharField(
        max_length=200
    )
    marketprice3 = models.CharField(
        max_length=200
    )
    class Meta:
        db_table="axf_mainshow"


class GoodsTypes(models.Model):
    typeid = models.CharField(
        max_length=40,
    )
    typename = models.CharField(
        max_length=10,
    )
    childtypenames = models.CharField(
        max_length=200,
    )
    typesort = models.IntegerField()
    class Meta:
        db_table="axf_foodtypes"



class Goods(models.Model):
    productid = models.CharField(
        max_length=20
    )
    productimg = models.CharField(
        max_length=200
    )
    productname = models.CharField(
        max_length=200,
        null=True,
    )
    productlongname = models.CharField(
        max_length=200,
    )
    isxf = models.BooleanField(
        default=0
    )
    pmdesc = models.BooleanField(
        default=0
    )
    specifics = models.CharField(
        max_length=20,
    )
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.IntegerField( )
    childcid = models.IntegerField()
    childcidname = models.CharField(
        max_length=30
    )
    dealerid = models.CharField(
        max_length=10
    )
    storenums = models.IntegerField()
    productnum = models.IntegerField()
    class Meta:
        db_table="axf_goods"





