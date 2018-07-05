from django.db import models

# Create your models here.

class Categary(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='分类名'
    )


class Item(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='商品',
        db_index=True

    )
    barcode = models.CharField(
        max_length=15,
        null=True,
        verbose_name='条码'
    )
    price = models.FloatField(
        verbose_name='售价'
    )
    in_price = models.DecimalField(
        max_digits=13,
        decimal_places=2,
        verbose_name='进货价'
    )
    come_in_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )
    update_time = models.DateTimeField(
        auto_now=True,
        verbose_name='修改时间'
    )
    icon = models.CharField(
        max_length=300,
        null=True,
        verbose_name='封皮'
    )
    categary = models.ForeignKey(
        Categary,
        verbose_name='所属分类',
        db_index=True
    )

    def __str__(self):
        return self.name


class Cart(models.Model):
    name = models.CharField(
        max_length=10,
        verbose_name='名字'
    )
    item = models.ForeignKey(
        Item,
        verbose_name='商品'
    )
    class Meta:
        db_table = 'cart'
        ordering = ['-id']  # 排序
