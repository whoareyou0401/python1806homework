from django.db import models

# Create your models here.

class Grade (models.Model):
    name = models.CharField(max_length=20,
                            verbose_name="班级"
                            )

    type = models.CharField(max_length=20,
                            verbose_name="类型"
                            )
    def __str__(self):
        return self.name


class Stu(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name="姓名"
                            )
    age = models.IntegerField(default=18,
                              verbose_name="年龄"
                              )
    score = models.IntegerField(verbose_name="成绩")

    grade = models.ForeignKey(Grade,
                              verbose_name="所属年纪",
                              null=True
                                  )

    def __str__(self):
        return self.name

