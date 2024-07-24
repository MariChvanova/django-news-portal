from .celery import app as celery_app
from celery import shared_task
import time

__all__ = ('celery_app',)

@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")

