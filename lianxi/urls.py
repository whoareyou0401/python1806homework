from django.conf.urls import url,include
from django.contrib import admin
from lianxi import views


urlpatterns = [
    url(r'^data$',views.my_data),

]