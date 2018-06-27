"""day02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from teach import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^test$", views.test),
    url(r"^cates$", views.cate_view),
    url(r"^items$", views.item_view),
    url(r"^item$", views.get_item),
    url(r"^item-search$", views.search_item_by_price),
    url(r"^item-search/name", views.search_item_by_name),
    url(r"^item-search/time$", views.search_item_by_time)
]
