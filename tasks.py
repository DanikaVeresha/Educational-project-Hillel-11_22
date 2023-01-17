import datetime
import os
from celery import Celery
import models_db
import all_db
from sqlalchemy.orm import Session
import requests_bank

rabbit_host = os.environ.get('RABBIT_HOST', 'localhost')
app = Celery('tasks', broker=f'pyamqp://guest@{rabbit_host}//')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(86400.0, get_bank_tasks.s(), name='add every 24 hours')


@app.task
def get_bank_tasks():
    requests_bank.PB_bank()


