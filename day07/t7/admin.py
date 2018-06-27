from django.contrib import admin
from t7.models import Stu,Grade,MyBook
# Register your models here.

class StuInfo(admin.TabularInline):
    model = Stu
    extra = 3
class GraddeAdmin(admin.ModelAdmin):
    inlines = [StuInfo]


class StuAdmin(admin.ModelAdmin):
    def is_old_man(self):
        if self.age >= 18:
            return "老年人"
        else:
            return "你还没熟"
    is_old_man.short_description = "是否成年"
    list_display = ['name','age','grade',is_old_man,] # 想要显示的列表
    list_filter = ['name', 'age'] # 过滤的字段列表
    search_fields = ['name']
    list_per_page = 3
    fieldsets = [
        ('基本信息',{'fields':['name','age']}),
        ('成绩',{'fields':["score"]})
    ]

#
# # admin.site.register(Stu, StuAdmin)
# admin.site.register(Stu)
# # admin.site.register(Grade)
# admin.site.register(Grade,GraddeAdmin)
#

class Mysite(admin.AdminSite):
    site_header = "今天又要做测评"
    site_title = "呵呵"
    site_url = "http://www.baidu.com"
mysite = Mysite()
mysite.register(Stu)
mysite.register(MyBook)

