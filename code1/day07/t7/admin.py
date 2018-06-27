from django.contrib import admin
# from django.forms import fields
# from django.contrib.contenttypes import fields
# from django.db.models import fields
# from django.contrib.gis.db.models import fieldsets
from t7.models import Stu, Grade, MyBook
# Register your models here.

class StuInfo(admin.TabularInline):
    model = Stu
    extra = 3

class GradeAdmin(admin.ModelAdmin):
    inlines = [StuInfo]

class StuAdmin(admin.ModelAdmin):

    def is_old_man(self):
        if self.age >= 18:
            return "老年人"
        else:
            return "你还不成熟"
    is_old_man.short_description = "是否成年"
    list_display = ['name', 'age', is_old_man] #想要显示的字段列表
    list_filter = ['name', 'age'] # 过滤条件列表
    search_fields = ['name']
    list_per_page = 3
    fieldsets = [
            ('基本信息', {"fields": ("name", "age")}),
            ('成绩', {"fields": ("score",)}),
    ]


# admin.site.register(Stu, StuAdmin)
# admin.site.register(Stu)
# # admin.site.register(Grade)
# admin.site.register(Grade, GradeAdmin)


class Mysite(admin.AdminSite):
    site_header = "今天又要做测评"
    site_title = "呵呵"
    site_url = "http://www.baidu.com"


mysite = Mysite()
mysite.register(Stu)
mysite.register(MyBook)