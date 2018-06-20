from django.db import models

# Create your models here.

class Grade(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="姓名",
        db_index=True
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="是否活跃"
    )
class Student(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="姓名",
        db_index=True
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )
    age = models.IntegerField(
        verbose_name="年龄"
    )
    score = models.FloatField(
        verbose_name="成绩"
    )
    grade = models.ForeignKey(
        Grade,
        verbose_name="班级id",
        db_index=True
    )
