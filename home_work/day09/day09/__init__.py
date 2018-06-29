from __future__ import absolute_import
import pymysql
from django.core.signals import request_started
from django.db.models.signals import pre_save
from django.dispatch import receiver
from t9.my_singals import action

from .celery import app as celery_app
pymysql.install_as_MySQLdb()

def pre_save_model(sender,**kwargs):
    print(sender)
    print(kwargs.get('instance'))#?
    my_instance = kwargs.get('instance')
    print(my_instance.data)
pre_save.connect(pre_save_model)


@receiver(request_started)
def my_req_started(sender,**kwargs):
    print(sender)
    print(kwargs)

def my_design_signal(sender,**kwargs):
    print(sender,kwargs)

action.connect(my_design_signal)

