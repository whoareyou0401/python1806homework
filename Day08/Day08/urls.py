"""Day08 URL Configuration

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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sendmail/', views.send_mail_ss),
    url(r'^my_send_mail/', views.my_send_mail),
    url(r'^htmlemail/', views.send_email_html),
    url(r'^email_verify/', views.get_verify_code),
    url(r'^verify/(.*)', views.verify)
]
