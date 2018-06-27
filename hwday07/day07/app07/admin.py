from django.contrib import admin
from app07.models import Stu,Grade
# Register your models here.


class StuInfo(admin.TabularInline):
    model = Stu
    extra = 3
class GradeAdmin(admin.ModelAdmin):
    inlines = [StuInfo,]



class StuAdmin(admin.ModelAdmin):
    def is_old_man(self):
        if self.age >= 18:
            return "老年人"
        else:
            return "o(*￣︶￣*)o"
    list_display = ["name","age"]
    list_filter = ["name","age"]
    search_fields = ["name"]
    list_per_page = 4
    fieldsets = [
        ('基本信息',{"fields":("name","age")}),
        ('成绩',{"fields":("score",)})
    ]









admin.site.register(Stu,StuAdmin)
admin.site.register(Grade,GradeAdmin)





