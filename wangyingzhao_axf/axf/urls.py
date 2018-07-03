
from django.conf.urls import url, include
from axf import views
urlpatterns = [
    url(r'home$', views.home, name='home'),
    url(r'market$', views.market, name='market'),
    url(r'market-with-param/(\d+)', views.market_with_param, name='market_with_param'),
    url(r'cart$', views.cart, name='cart'),
    url(r'mine$', views.mine, name='mine')
]
