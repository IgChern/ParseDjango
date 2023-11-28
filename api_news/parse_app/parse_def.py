import requests
from datetime import datetime
from parse_app.models import Post

import logging

logger = logging.getLogger(__name__)


def parse_request():
    '''
    This script fetches the IDs of the top 30 stories from website.
    Make relevant data (title, url, date) in model Post.
    '''
    try:
        # URL to fetch the IDs of the stories
        urlall = f'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
        alljson_id = requests.get(urlall).json()

        # Itearate through the first 30 stories by ID
        for id in alljson_id[:31]:
            # URL to fetch details of a specific ID
            urlid = f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty'
            onejson_id = requests.get(urlid).json()

            # Make information from story
            title = onejson_id.get('title')
            url = onejson_id.get('url')
            dateunix = onejson_id.get('time')

            # Convert from UNIX date to ISO 8601
            dateutc = datetime.fromtimestamp(dateunix)
            dateiso = dateutc.isoformat()

            # Check the URL is being
            if url is not None and url != '':

                # Create post
                post = {'title': title,
                        'url': url,
                        'created': dateiso
                        }

                # Check if a post in the database exists
                if not Post.objects.filter(title=title).exists():
                    # Create a new Post obj in database
                    newpost = Post.objects.create(**post)

        return True
    # Log any errors
    except Exception as e:
        logger.error(f"An error: {e}")
        return None
