from __future__ import absolute_import
from celery import Celery,platforms
from django.conf import settings
platforms.C_FORCE_ROOT = True
import os
os.environ.setdefault("DJANGO_SETTING_MODULE","day09.settings")
app = Celery("mycelery")
app.conf.timezone = "Asia/Shanghai"
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)#你需要在app目录下新建task.py的文件