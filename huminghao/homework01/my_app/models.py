from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class School(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    school = models.ForeignKey(School)