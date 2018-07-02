from django.db import models

# Create your models here.
class BaseData(models.Model):
    img = models.CharField(
    max_length = 255,
    verbose_name = '图片链接'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='介绍名字'
    )
    trackid = models.CharField(
        max_length=100,
        verbose_name='trackid'
    )

    class Meta:
        abstract = True


class Wheel(BaseData):
    class Meta:
        db_table = "axf_wheel"