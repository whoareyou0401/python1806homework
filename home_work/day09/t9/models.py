from django.db import models

# Create your models here.
class MyData(models.Model):
    data = models.CharField(
        max_length=20
    )
    my_time = models.DateTimeField(
        auto_now_add=True
    )
