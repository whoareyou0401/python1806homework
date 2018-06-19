from django.shortcuts import render
from tapp.models import *
# Create your views here.

def my_student(req):
    student = Student.objects.all()
    return render(req,"student.html",context={"student":student})

def first(req):
    return render(req,"hellodjango.html")