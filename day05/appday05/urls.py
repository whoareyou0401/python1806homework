from django.conf.urls import url
from django.contrib import admin
from appday05.views import *

urlpatterns = {
    url(r"^index$", index),
    url(r'^my-response$', my_response),
    url(r"^my-json$", my_json),
    url(r"^t5_index$", t5_index),
    url(r"^logout$", logout, name='logout'),
    url(r"^login$", login, name='login')
    #  三个”logout“依次代表网址、 这个网址对应的哪个试图解决、  反向解析的时候用的。

}