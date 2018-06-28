from django.db import models

# Create your models here.
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
        verbose_name="成绩",
        null = True
    )