import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_news.settings')

app = Celery('api_news')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
