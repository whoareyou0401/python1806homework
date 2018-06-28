from django.db import models
import random
# Create your models here.

class StuManger(models.Manager):
    def create_stu(self):
        stu = Stu()
        stu.name = "张三" + str(random.randrange(30))
        stu.age = random.randrange(100)
        stu.grade = random.randint(60, 100)
        stu.save()
        return stu

class Stu(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="名字"
    )
    age = models.IntegerField(
        default=7,
        verbose_name="年纪"
    )
    grade = models.IntegerField(
        verbose_name="成绩",
        null=True
    )
    my_manage = StuManger()
    my_manage1 = models.Manager()
    def __str__(self):
        return self.name
    class Meta:
        db_table = "stu"

class IdCard(models.Model):
    num = models.CharField(max_length=20)
    org = models.CharField(max_length=40)

class Person(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="人名"
    )
    age = models.IntegerField(
        default=1,
        verbose_name="年纪"
    )
    id_card = models.OneToOneField(
        IdCard,
        verbose_name="身份证",
        on_delete=models.PROTECT
    )

class Team(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="队名"
    )
    desc = models.CharField(
        max_length=200,
        null=True,
        verbose_name="描述"
    )

class player(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="人名"
    )
    age = models.IntegerField(
        default=5,
        verbose_name="年龄"
    )
    team = models.ForeignKey(
        Team,
        null=True,
        on_delete=models.SET_NULL
    )

class Author(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="名字"
    )
    age = models.IntegerField(
        default=5,
        verbose_name="年龄"
    )

class Book(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name="书名"
    )
    authors = models.ManyToManyField(
        Author,
        verbose_name="作者"
    )

class Animal(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="名字"
    )
    sex = models.CharField(
        max_length=4,
        default="雌性"
    )
    class Meta:
        abstract=True

class Dog(Animal):
    hobby = models.CharField(
        max_length=20,
        verbose_name="爱好"
    )

class Cat(Animal):
    eat = models.CharField(
        max_length=20,
        verbose_name="吃"
    )

class Roadgj(models.Model):
    speed = models.IntegerField(
        default=10
    )
    humens = models.IntegerField(
        default=1
    )

class Car(Roadgj):
    brand = models.CharField(
        max_length=20
    )

class FireCar(Roadgj):
    time = models.TimeField(
        auto_now_add=True
    )