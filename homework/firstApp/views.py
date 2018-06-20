import random

from django.http import HttpResponse
from django.shortcuts import render
from firstApp.models import *

# Create your views here.

def add_grade(request):
    grade = Grade()
    num = random.randrange(1000)
    grade.name="python%d班" % num
    grade.save()
    return HttpResponse("班级: %s 添加成功" % grade.name)

def add_student(request):
    grade = Grade.objects.last()
    student = Student()
    num = random.randrange(1000)
    num_age = random.randrange(30)
    num_score = random.randrange(100)
    student.name="老王%d号" % num
    student.age = num_age
    student.score =num_score
    student.grade = grade
    student.save()
    return HttpResponse("学生:%s 添加成功"%student.name)

def get_grades(request):
    grades = Grade.objects.all()
    data = {
        "grades": grades
    }
    return render(request, 'getGrades.html',context=data)

def get_students(request):
    students = Student.objects.all()
    data = {
        "students":students,
    }
    return  render(request, 'getStudents.html', context=data)

def get_student(request):
    gradeid = request.GET.get("gradeid")
    students = Student.objects.filter(grade=gradeid)
    data = {
        "students": students,
    }
    return render(request, 'getStudents.html', context=data)