from  django.contrib import admin

from django.contrib.gis.db.models import fieldsets
from t7.models import Stu, Grade, MyBook
# Register your models here.

class StuInfo(admin.TabularInline):
    model = Stu
    extra = 2


class GradeAdmin(admin.ModelAdmin):
    inlines = [StuInfo]

class StuAdmin(admin.ModelAdmin):

    def is_old_man(self):
        if self.age >=18:
            return "老年人"
        else:
            return "你还不成熟"

    is_old_man.short_description = "是否成年"
    list_display = ['name', 'age', is_old_man]
    list_filter = ['name', 'age']
    search_fields = ['name']
    list_per_page = 3
    fieldsets = [
        ('基本信息', {"fields":("name", "age")}),
        ('成绩',{"fields":("name","age")}),
    ]





# admin.site.register(Stu. StuAdmin)
admin.site.register(Stu)
admin.site.register(Grade)
# admin.site.register(Grade. GradeAdmin)

class Mysite(admin.AdminSite):
    site_header = '今天要做测评'
    site_title = "呵呵"
    site_url = "http://www.baidu.com"

mysite = Mysite()  # 实例化
mysite.register(Stu)  # 注册
mysite.register(MyBook)