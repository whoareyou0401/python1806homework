from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render
from t3.models import *

# Create your views here.

def get_avg_age(req):
    s = Stu.objects.aggregate(Avg("age"))
    print(s)
    return HttpResponse(s.get('age__avg'))