from django.conf.urls import url
from akaizi import views

urlpatterns = [
    url(r'^avg-age$', views.get_avg_age)
]