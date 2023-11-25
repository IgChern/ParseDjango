from .models import Post
from django.http import JsonResponse
from .parse_def import parse_request


def get_posts(request):
    parse_request()

    list_of_fields = [field.name for field in Post._meta.get_fields()]

    order_by = request.GET.get('order', 'created')

    if order_by.startswith('-'):
        direction = '-'
    else:
        direction = ''

    field_name = order_by.lstrip('-')

    try:
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 5))
        if limit > 30 or limit <= 0:
            return JsonResponse({'Error': 'Invalid limit, must be a positive integer and max 30'}, status=400)
    except ValueError:
        return JsonResponse({'Error': 'Invaild offset or limit(need int)'}, status=400)

    if field_name not in list_of_fields:
        return JsonResponse({'Error': 'Invalid field name for sorting'}, status=400)

    order_by = f'{direction}{field_name}'

    posts = Post.objects.all().order_by(order_by)[offset: offset+limit]

    data = [{'title': post.title, 'url': post.url, 'created': post.created}
            for post in posts]
    return JsonResponse(data, safe=False)
