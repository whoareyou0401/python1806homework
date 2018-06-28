from django.db.models import F, Q
from django.forms import model_to_dict
from django.http import HttpResponse
from t3.models import *
import json

def get_age_gt_grade(req):
    result = Stu.my_manage.filter(age__gt=F('grade'))
    res = [model_to_dict(i) for i in result]
    return HttpResponse(json.dumps(res))

def get_age_and_grade(req):
    s = Stu.objects.filter(Q(age__lt=50) & Q(grade__gt=60))
    print(s)
    return HttpResponse("ok")

def add_stu(req):
    stu = Stu.my_manage.create_stu()
    return HttpResponse(stu.name)

def get_hunmen(req):
    p = Person.objects.last()
    card = p.id_card
    card_dict = model_to_dict(card)
    return HttpResponse(json.dumps(card_dict))

def delete_humen(req):
    # 获取所有求情参数
    params = req.GET
    # 获取h_id
    h_id = params.get("h_id")
    try:
        # 根据id获取人的对象
        p = Person.objects.get(pk=int(h_id))
        # 获取到对象后删除对象
        p.delete()
        return HttpResponse("数据真没啦")
    except:
        return  HttpResponse("兄弟，你错了")

def delete_idcard(req):
    idcard = IdCard.objects.last()
    idcard.delete()
    return HttpResponse("搞定")

def get_team_players(req):
    params = req.GET
    team_id = params.get("t_id")
    team = Team.objects.get(id=int(team_id))
    # 级联获取数据 相关联对象名的小写_set.all() filter
    players = team.player_set.all()
    res = [model_to_dict(i) for i in players]
    return HttpResponse(json.dumps(res))

def get_book_by_author(req):
    a_id = req.GET.get("a_id")
    author = Author.objects.get(pk=int(a_id))
    books = author.book_set.all().values("title")
    # print(books)
    # res = [model_to_dict(b) for b in books]
    # print(res)
    return HttpResponse(books)

def get_authors_by_book(req):
    # 获取参数b_id 如果获取不到就设置成3
    b_id = req.GET.get("b_id", 3)
    book = Book.objects.get(pk=b_id)
    # 通过数据找作者
    authors = book.authors.all()
    print(authors)
    res = [model_to_dict(a) for a in authors]
    return HttpResponse(json.dumps(res))
