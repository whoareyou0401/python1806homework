from django.conf.urls import url
from teach import views

urlpatterns = [
    url(r'^index$', views.index, name="index"),
    url(r'^my-response$', views.my_response, name="my_response"),
    url(r'^my-json$', views.my_json, name="my_json"),
    # 用户系统
    url(r'^t5_index$', views.t5_index, name="t5_index"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^login$', views.login, name="login"),
]
