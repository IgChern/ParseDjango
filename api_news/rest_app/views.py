from rest_framework import viewsets
from .myordering import CustomOrderingFilter
from parse_app.models import Post
from .serializers import PostSerializer
from .mypagination import CustomPag
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    '''
    This class includes:
    - queryset to set view of Post model
    - serializer_class to transform Post model to JSON
    - pagination_class to paginate the serialize output
    - filter_backends filers order
    - ordering_fields from parse_app Post model fields
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPag
    filter_backends = [CustomOrderingFilter]
    ordering_fields = [field.name for field in Post._meta.get_fields()]
