from .parse_def import parse_request
from celery import shared_task


@shared_task
def get_parsed():
    post = parse_request()
    if post:
        return post
    else:
        return None