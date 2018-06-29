from django.db import models

# Create your models here.
class Stu(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="名字"
    )
    age = models.IntegerField(
        default=7,
        verbose_name="年纪"
    )
    class Meta:
        db_table = "stu"
