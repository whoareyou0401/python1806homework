from django.contrib import admin
from t7.models import Stu,Grade,MyBook
# Register your models here.

class StuInfo(admin.TabularInline):
    model = Stu
    extra = 3

class GradeAdmin(admin.ModelAdmin):
    inlines = [StuInfo]


class StuAdmin(admin.ModelAdmin):
    #对字段数据进行二次加工判断
    def is_old_man(self):   #?
        if self.age >= 18:
            return "老年人"
        else:
            return "你还不成熟"
    #对函数做简短描述
    is_old_man.short_description = "是否成年"
    list_display = ['name','age',is_old_man]#想要显示的列表
    list_filter = ['name','age']#过滤条件列表
    search_fields = ['name']
    #设置每页数据（分页）
    list_per_page = 3
    #将字段按照分组的方式去显示
    fieldsets = [
        ("基本信息",{'fields':('name','age')}),
        ("成绩", {'fields': ('score',)}),
    ]

class Mysite(admin.AdminSite):
    site_header = "今天又要做测评"
    site_title = "呵呵"
    site_url = "https://www.baidu.com/"
mysite = Mysite()
mysite.register(Stu)
mysite.register(MyBook)



# admin.site.register(Stu,StuAdmin)  #?
# admin.site.register(Stu)  #?
# admin.site.register(Grade)
# admin.site.register(Grade,GradeAdmin)
