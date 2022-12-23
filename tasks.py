import datetime
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(86400.0, add.s(x=75.7659, y=25.7845), name='add every 24 hours')


@app.task
def add(x, y):
    print(x + y)
    with open('celery.csv', 'w') as f:
        f.write(f'x + y = {x + y} / {datetime.datetime.now()}')
    return x + y

