from django.conf.urls import url
from django.contrib import admin
from akai import views

urlpatterns = [
    url(r'^language$', views.language_view),
    url(r'^language-v2$', views.language_v2_view)
]