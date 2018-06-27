from django.contrib import admin
from lianxi.models import Stu,Grade
# Register your models here.
#
# class StuInfo(admin.TabularInline):
#     module=Stu
# class GradeInfo(admin.ModelAdmin):
#     inlines = [StuInfo]
#
#
#
# class StuAdmin(admin.ModelAdmin):
#     def old_man(self):
#         if self.age>18:
#             return 'old man'
#         else:
#             return 'yung man'
#     old_man.short_description = "yuang or old"
#     list_display = ['name','age']
#     list_filter =['name','age']
#     search_fields = ['name']
#     list_per_page = 3
#     ordering = ['age.'
#                 '']
#     fieldsets = (
#         ('基本信息',{"fields":('name','age')}),
#     )
#
#
#
# admin.site.register(Stu,StuAdmin)
# admin.site.register(Grade,GradeInfo)