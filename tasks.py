import datetime
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    print(x + y)
    with open('test.csv', 'w') as f:
        f.write(f'x + y = {x + y} {datetime.datetime.now()}')
    return x + y
