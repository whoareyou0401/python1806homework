from django.db import models

# Create your models here.

class Stu(models.Model):
    s_name = models.CharField(
        max_length=30,
        verbose_name="学生名字"
    )
    icon = models.ImageField(
        upload_to="icons"
    )