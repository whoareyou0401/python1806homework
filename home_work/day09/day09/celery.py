from __future__ import absolute_import
from celery import Celery, platforms
from django.conf import settings
import os
platforms.C_FORCE_ROOT = True
os.environ.setdefault("DJANGO_SETTING_MODULE","day09.settings")
# CELERY_TIMEZONE = 'Asia/Shanghai'
app = Celery('test')
app.conf.timezone = "Asia/Shanghai"
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)