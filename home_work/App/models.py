from django.db import models

# Create your models here.
class Myclass (models.Model):
    name = models.CharField(max_length=30,verbose_name="班名",db_index=True)
    ctime = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    isactive = models.BooleanField(verbose_name="活跃度")
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=30,verbose_name="姓名",db_index=True)
    stime = models.DateTimeField(auto_now_add=True, verbose_name="进班时间")
    age = models.IntegerField(verbose_name="年龄")
    grade= models.FloatField(verbose_name="成绩")
    cid = models.ForeignKey(Myclass,verbose_name="班级ID",db_index=True)
    def __str__(self):
        return  self.name