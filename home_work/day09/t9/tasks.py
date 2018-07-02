import random

from celery import task
import time
from .models import MyData

@task
def hello_celery(loop):
		print('hello')
		time.sleep(2)
@task
def get_data_with_param(loop):
    for i in range(loop):
        time.sleep(2)
        print("我被执行了"+str(i))

@task
def create_data():
    num = random.randrange(100)
    MyData.objects.create(data = str(num))
