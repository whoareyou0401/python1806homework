from django.contrib import admin
from t7.models import Stu, Grade
# Register your models here.


class StuAdmin(admin.ModelAdmin):
    def is_old_man(self):
        if self.age >= 18:
            return "老年人"
        else:
            return "小孩崽子"

    is_old_man.short_description = "是否成年"
    list_display = ['name','age', is_old_man]
    list_filter = ['name','age']
    search_fields = ['name']
    list_per_page = 3
    fieldsets = [
        ('基本信息', {"fields": ('name','age')}),
        ('成绩', {"fields": ('score',)}),
]


# admin.site.register(Stu, StuAdmin)
admin.site.register(Stu)
admin.site.register(Grade)