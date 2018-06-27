from django.conf.urls import url
from t6 import views

urlpatterns = [
    url(r'^hello$',views.hello),
    url(r'lucky$',views.luck),
    url(r'^userinfo$',views.userinfo)
]