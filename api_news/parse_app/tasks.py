from .parse_def import parse_request
from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def get_parsed():
    '''
    This Celery task decorated with @shared task,
    It calls parse_request function to store parsed data.
    If success, return success message.
    '''
    try:
        # Call the parse_request function for storing data
        post = parse_request()
        # Check if the parsing successfull
        if post:
            return 'Parsing success'
        else:
            return None
    except Exception as e:
        logger.error(f"An error: {e}")
        return None
