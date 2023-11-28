from .models import Post
from django.http import JsonResponse


def get_posts(request):
    '''
    This view function make and returns list of posts from the
    database with parameters (order, offset, limit).
    It includes validation of parameters.
    '''
    # Get the list of fields from Post model
    list_of_fields = [field.name for field in Post._meta.get_fields()]

    # Get the 'order' parameter, default by 'created'
    order_by = request.GET.get('order', 'created')

    # Check sorting direction
    if order_by.startswith('-'):
        direction = '-'
    else:
        direction = ''

    # Delete '-' if exists
    field_name = order_by.lstrip('-')

    try:
        # Offset and limit parameters with default values
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 5))

        # Validate limit and offset
        if limit > 30 or limit <= 0:
            return JsonResponse({'Error': 'Invalid limit, must be a positive integer and max 30'}, status=400)
        if offset < 0:
            return JsonResponse({'Error': 'Invalid offset, must be a positive integer'}, status=400)
    except ValueError:
        return JsonResponse({'Error': 'Invaild offset or limit(need int)'}, status=400)

    # Check if the specific name is valid for sorting
    if field_name not in list_of_fields:
        return JsonResponse({'Error': 'Invalid field name for sorting'}, status=400)

    # Make the final direction and field name
    order_by = f'{direction}{field_name}'

    # Make posts from database with sorting, offset and limit
    posts = Post.objects.all().order_by(order_by)[offset: offset+limit]

    # Convert data to list of dictionaries
    data = [{'title': post.title, 'url': post.url, 'created': post.created}
            for post in posts]

    # Return the data as JSON
    return JsonResponse(data, safe=False)
