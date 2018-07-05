from django.conf.urls import url
from AXF1806 import views

urlpatterns=[
    url(r'^home$', views.home, name='home'),
    url(r'^market$', views.market, name='market'),
    url(r'^market-with-param/(\d+)/(\d+)/(\d+)', views.market_with_param, name='market_with_param'),
    url(r'^cart$', views.cart, name='cart'),
    url(r'^mine$', views.mine, name='mine'),
    # url(r'^register$', views.RegisterAPI.as_view(), name='register'),
    url(r"^register$", views.RegisterAPI.as_view(), name="register"),

    url(r"^login$", views.LoginApi.as_view(), name="login"),
    url(r"^active/(.+)", views.active, name="active")
]