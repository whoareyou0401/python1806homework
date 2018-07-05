from django.contrib import admin
from t7.models import Stu, Grade

# Register your models here.


class StuInfo(admin.TabularInline):
    model = Stu
    extra = 3


class GradeAdmin(admin.ModelAdmin):
    inlines = [StuInfo, ]
#
#
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




# admin.site.register(Stu, StuAdmin)
admin.site.register(Stu)
# admin.site.register(Grade)
admin.site.register(Grade, GradeAdmin)

# class Mysite(admin.AdminSite):
#     site_header = '今天真美'
#
#
# mysite = Mysite()
# mysite.register(Stu)
