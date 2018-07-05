from django.db import models
import random
# Create your models here.


class StuManager(models.Manager):
    def create_stu(self):
        stu = Stu()
        stu.name = '张三'+ str(random.randrange(30))
        stu.age = random.randrange(100)
        stu.grade = random.randint(50, 150)
        stu.save()
        return stu

class Stu(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="姓名"
    )
    age = models.IntegerField(
        default=7,
        verbose_name="年龄"
    )
    grade = models.IntegerField(
        verbose_name='成绩',
        null=True
    )
    my_manage = StuManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "stu"



# class IdCard(models.Model):
#     num = models.CharField(
#         max_length=30
#     )
#     org = models.CharField(max_length=40)
#
#
# class Person(models.Model):
#     name = models.CharField(
#         max_length=30,
#         verbose_name='人名'
#     )
#     age = models.IntegerField(
#         default=1,
#         verbose_name='年纪'
#     )
#     id_card = models.OneToOneField(
#         IdCard,
#         verbose_name='身份证',
#         on_delete=models.PROTECT
#     )
#
#
# class Team(models.Model):
#     name = models.CharField(
#         max_length=30,
#         verbose_name='队名'
#     )
#     desc = models.CharField(
#         max_length=200,
#         null=True,
#         verbose_name='描述'
#     )
#
# class player(models.Model):
#     name = models.CharField(
#         max_length=30,
#         verbose_name='人名'
#     )
#     age = models.IntegerField(
#         default=5,
#         verbose_name='年纪'
#     )
#
# class  Author(models.Model):
#     name = models.CharField(
#         max_length=30,
#         verbose_name='人名'
#     )
#     age = models.IntegerField(
#         default=5,
#         verbose_name='年纪'
#     )
#
#
#
# class Book(models.Model):
#     title = models.CharField(
#         max_length=30,
#         verbose_name='书名'
#     )
#     authors = models.ManyToManyField(
#         Author,
#         verbose_name='作者'
#     )

