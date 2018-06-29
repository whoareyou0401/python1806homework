from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()


class Company(models.Model):
    name = models.CharField(max_length=50,verbose_name="公司名称")
    address = models.CharField(max_length=50,verbose_name="公司地址")

class Staff(models.Model):
    name = models.CharField(max_length=(30),verbose_name="姓名")
    position = models.CharField(max_length=(20))
    company = models.ForeignKey(Company)