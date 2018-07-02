from django.conf.urls import url
from t6_paginator import views

urlpatterns = [
    url(r'^student/(\d+)$',views.stu_list,name="student")
]