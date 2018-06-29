from django.contrib import admin
from App.models import Stu,Grade,MyBook
# Register your models here.
class StuInfo(admin.TabularInline):
    model=Stu
    extra = 3
class GradeAdmin(admin.ModelAdmin):
    inlines = [StuInfo]

class StuAdmin(admin.ModelAdmin):
    def is_old_man(self):
        if self.age>=18:
            return ('老年人')
        else:
            return ('你还不成熟')

    list_display = ['name','age',is_old_man]
    list_filter = ['name','age']#过滤的字段列表
    search_fields = ['name']
    list_per_page = 3
    fieldsets = [  ("基本信息",{"fields":("name","age")}),
                   ("成绩",{"fields":("score",)})]
class Mysite(admin.AdminSite):
    site_header="今天又测评了"
    site_title="呵呵"
mysite=Mysite()
mysite.register(Stu)
mysite.register(MyBook)



#admin.site.register(Stu)
#admin.site.register(Grade,GradeAdmin)
