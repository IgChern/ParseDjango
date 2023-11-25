import requests
from datetime import datetime
from parse_app.models import Post


def parse_request():
    urlall = f'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
    alljson_id = requests.get(urlall).json()
    for id in alljson_id[:31]:
        urlid = f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty'
        onejson_id = requests.get(urlid).json()
        title = onejson_id.get('title')
        url = onejson_id.get('url')
        dateunix = onejson_id.get('time')
        dateutc = datetime.fromtimestamp(dateunix)
        dateiso = dateutc.isoformat()
        post = {'title': title,
                'url': url,
                'created': dateiso
                }
        if not Post.objects.filter(title=title).exists():
            newpost = Post.objects.create(**post)
            return newpost
