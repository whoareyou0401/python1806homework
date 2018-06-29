import json
from django.core.management.commands.diffsettings import module_to_dict
from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import render
from pp.models import *



def get_age_gt_grade(req):
    res = Stu.objects.filter(age__gt=F('grade'))
    result = [module_to_dict(i) for i in res]
    return HttpResponse(json.dumps(result))

def get_age_grade(req):
    res = Stu.objects.filter(age__gt=F('grade'))
    result = [module_to_dict(i) for i in res]
    return render(req, "stu_age_grade.html", context={"stu": result})


def get_age_and_grade(req):
    res = Stu.objects.filter(Q(age__lt =60) & Q(grade__gt = 70))
    print(res)
    return HttpResponse("ok")