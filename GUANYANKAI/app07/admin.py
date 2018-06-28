from django.contrib import admin
from app07.models import Stu, Grade
from app07.models import MyBook

# Register your models here.
# from django.forms import fields
class StuInfo(admin.TabularInline):
    model = Stu
    extra = 3

class GradeAdmin(admin.ModelAdmin):
    inlines = [StuInfo]

class StuAdmin(admin.ModelAdmin):
    def is_old_man(self):
        if self.age >= 18:
            return "老腊肉"
        else:
            return "小鲜肉"
    list_display = ['name', 'age', is_old_man] # 想要显示的列表
    list_filter = ['name', 'age'] # 过滤条件列表
    search_fields = ['name'] #
    list_per_page = 3
    fieldsets = (
        ('基本信息', {'fields': ('name', 'age')}),
        ('成绩', {'fields': ('score',)}),
    )

# admin.site.register(Grade)
# admin.site.register(Stu)
admin.site.register(Stu, StuAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(MyBook)

# class Mysite(admin.AdminSite):
#     site_header = "阳光灿烂"
#     site_title = "的O(∩_∩)O哈哈~"
# site_urls = "http://www.baidu.com"
# mysite = Mysite()
# mysite.register(Stu)