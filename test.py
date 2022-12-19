from flask import Flask
from celery import Celery


def make_celery(asd):
    celery = Celery(asd.import_name)
    celery.conf.update(asd.config["CELERY_CONFIG"])

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with asd.asd_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


flask_asd = Flask(__name__)
flask_asd.config.update(CELERY_CONFIG={
    'broker_url': 'redis://localhost:6379',
    'result_backend': 'redis://localhost:6379',
})
celery = make_celery(flask_asd)


@celery.task()
def add_together(a, b):
    return a + b


result = add_together.delay(23, 42)
result.wait()

