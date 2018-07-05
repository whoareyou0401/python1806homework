from django.db.models import F, Q
from django.forms import model_to_dict
from django.http import HttpResponse
from akaizi.models import *
import json


def get_age_gt_grade(req):
    result = Stu.my_manage.filter(age__gt=F('grade'))
    # model_to_dict
    print(result)
    res = [model_to_dict(i) for i in result]
    return HttpResponse(json.dumps(res))


def get_age_and_grade(req):
    s = Stu.my_manage.filter(Q(age__lt=50) | Q(grade__gt=50))
    print(s)
    return HttpResponse("ok")


def add_stu(req):
    stu = Stu.my_manage.create_stu()
    return HttpResponse(stu.name)


# def get_humen(req):
#     p = Person.objects.last()
#     card = p.id_ccard
#     card_dict = model_to_dict(card)
#     return HttpResponse(json.dumps(card_dict))
#
#
# def delete_humen(req):
#     # 获取所有的请求参数
#     params = req.GET
#     # 获取 h_id
#     h_id = params.get('h_id')
#     try:
#         Person.objects.get(pk=int(h_id))
#         p.delete()
#         return HttpResponse('数据丢了')
#     except:
#         return HttpResponse("兄弟，打他！")
#
#
# def delete_idcard(req):
#     idcard = IdCard.objects.last()
#     idcard.delete()
#     return HttpResponse('搞定了')
#
#
# def get_team_players(req):
#     params = req.GET
#     team_id = params.get('t-id')
#     team = Team.objects.get(id=int(team_id))
#     # 级联获取数据
#     players = team.player_set.all()
#     # print(players)
#     res = [model_to_dict(i) for i in players]
#     return HttpResponse(json.dumps(res))
#
# def get_book_by_author(req):
#     a_id = req.GET.get('a_id')
#     author = Author.objects.get(pk=int(a_id))
#     books = author.book_set.all().values('title')
#     # res = [model_to_dict(b) for b in books]
#     return HttpResponse(books)


