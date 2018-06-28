from django.core.paginator import Paginator
from django.shortcuts import render
from t6.models import Stu

# Create your views here.

def stu_list(req,page_num):
    if req.method =="GET":
        all_stu = Stu.objects.all()
        paginator = Paginator(all_stu,3)

        data_list = []
        try:
            page = paginator.page(page_num)
            data_list = page.object_list
        except:
            pass
        return render(req,"student.html",context={"stu_list":data_list,'page_range':paginator.page_range,'page': page})