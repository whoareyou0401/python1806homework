from django.conf.urls import url
from t5_auth.views import *

urlpatterns = [
    url(r'register$', register, name="register"),
    url(r'login$', login_api, name="login"),
    url(r'^welcome$', welcome_vip, name="welcome_vip"),
    url(r'^index', index, name="index"),
    url(r'^logout', logout, name="logout"),

]
