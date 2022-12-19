from flask import Flask
from celery import Celery


# def make_celery(asd):
#     celery = Celery(asd.import_name)
#     celery.conf.update(asd.config["CELERY_CONFIG"])
#
#     class ContextTask(celery.Task):
#         def __call__(self, *args, **kwargs):
#             with asd.asd_context():
#                 return self.run(*args, **kwargs)
#
#     celery.Task = ContextTask
#     return celery
#
#
# flask_asd = Flask(__name__)
# flask_asd.config.update(CELERY_CONFIG={
#     'broker_url': 'redis://localhost:6379/0',
#     'result_backend': 'redis://localhost:6379/0',
# })
# celery = make_celery(flask_asd)
#
#
# @celery.task()
# def add_together(a, b):
#     return a + b
#
#
# result = add_together.delay(23, 42)
# result.wait()

app = Flask(__name__)


@app.route("/home")
def home():
    a = 1
    b = 2
    d = a + b
    return f'hello, {d}'


app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'


celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

if __name__ == "__main__":
    app.run(debug=True)
