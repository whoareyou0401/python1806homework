"""day08 URL Configuration

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
from t8 import views
from email_verfiry import views as evs
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^email$',views.send_my_mail),
    url(r'^ems$', views.send_emailss),
    url(r'^htmlems$',views.send_my_mail),
    url(r'^text$',evs.get_verify_code),
    url(r'^verify/(.+)',evs.verify),
    url(r'^textlog$',views.test_log)
]
