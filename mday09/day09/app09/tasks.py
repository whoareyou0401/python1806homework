import random

from celery import task
from .models import MyData
import time
@task
def get_data():
    time.sleep(3)
    print("I am running")
@task
def get_data_with_param(loop):
    for i in range (loop):
        time.sleep(2)
        print("我被执行"+str(i))
@task
def cteate_data():
    num = random.randrange(100)
    MyData.objects.create(data=str(num))
