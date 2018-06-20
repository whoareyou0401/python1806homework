from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import School

# Create your views here.
def testone(req):
    return HttpResponse("这些是啥，那些又是啥")

def my_school(req):
    sch_infor = School.objects.all()
    return render(req,"school_infor.html",context={"schools":sch_infor})