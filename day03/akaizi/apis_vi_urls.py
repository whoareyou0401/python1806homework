from django.conf.urls import url
from akaizi import apis_v1 as apisv1

urlpatterns = [
    url(r'^get-stu$', apisv1.get_age_gt_grade),
    url(r'^get-age-grade$', apisv1.get_age_and_grade),
    url(r'^add-stu$', apisv1.add_stu),
    # url(r'^gethumen$', apisv1.get_humen),
    # url(r'^del-humen$', apisv1.delete_humen),
    # url(r'^del-card$', apisv1.delete_idcard),
    # url(r'^get-players', apisv1.get_team_players),
    # url(r'^get-book-by-author$', apisv1.get_book_by_author)

]