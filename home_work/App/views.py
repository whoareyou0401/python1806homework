from django.shortcuts import render
from django.http import HttpResponse
from App.models import *
# Create your views here.
def search(seq):
    myclass=Myclass.objects.all()
    return render(seq,'test.html',context={'myclass':myclass})

def students(req):
    students_id=req.GET.get('classid')
    studentt=Student.objects.all()
    studentt=studentt.filter(cid_id=students_id)
    return render(req,'student.html',context={'students':studentt})