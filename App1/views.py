from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
import logging
# Create your views here.

def my_email(req):
    title = '阿里'
    massg = '入职阿里'
    from_email = '15247328203@163.com'
    to_email = ['15247328203@163.com']
    send_mail(title,massg,from_email,to_email)
    return HttpResponse("ik")

def test_log(req):
    logger = logging.getLogger("django")
    logger.warning("this is python1806")
    return HttpResponse("OK")