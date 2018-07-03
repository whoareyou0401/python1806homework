from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    grade = models.IntegerField()
    s_class = models.CharField(max_length=30)


