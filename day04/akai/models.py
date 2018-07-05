from django.db import models


# Create your models here.
class ComLanguage(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='语言名字'
    )
    desc = models.CharField(
        max_length=200,
        verbose_name='描述',
        null=True

    )
    def get_desc(self):
        return self.desc


class Engineer(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='工程师'
    )
    sex = models.CharField(
        max_length=4,
        default='男'
    )
    comlanguage = models.ForeignKey(
        ComLanguage,
        verbose_name='编程语言'
    )
    start = models.DateTimeField(
        auto_now_add=True,
        verbose_name='从业时间'
    )

