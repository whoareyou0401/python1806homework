from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=30,
                            verbose_name="名字")
    address = models.CharField(max_length=30,
                               verbose_name="地址")

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    school = models.ForeignKey(School)
