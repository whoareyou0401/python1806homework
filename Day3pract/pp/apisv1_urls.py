from django.conf.urls import url
from pp import apis_v1 as apisv1



urlpatterns = [
    url(r'^get_stu/', apisv1.get_age_gt_grade),
    url(r'^ltage', apisv1.get_age_and_grade),
    url(r'^lt__age', apisv1.get_age_grade)
]