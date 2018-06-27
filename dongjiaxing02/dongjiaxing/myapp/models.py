from django.db import models

# Create your models here.
class Class(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="班级名"
    )
    creat_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )
    active = models.BooleanField()

class student(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="学生名"
    )
    creat_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )
    age = models.IntegerField(
        verbose_name="年龄"
    )
    score = models.FloatField(
        verbose_name="成绩"
    )
    class_id = models.ForeignKey(
        Class,
        verbose_name="班级id"
    )
