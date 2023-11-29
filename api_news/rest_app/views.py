from rest_framework import viewsets, filters, serializers
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

    filter_backends = [filters.OrderingFilter]
    ordering_fields = [field.name for field in Post._meta.get_fields()]

    def get_queryset(self):
        '''
        Method get_queryset writes the set to following order
        '''
        queryset = super().get_queryset()

        # Get list of order=''
        order_fields = self.request.query_params.getlist('order')
        if order_fields:
            # Check if 0st element has '-'
            if order_fields[0].startswith('-'):
                direction = '-'
            else:
                direction = ''

            # Make field name without '-'
            field_name = order_fields[0].lstrip('-')

            # Check if order field does not exists in order_field list from Post model
            invalid_field = False
            for _ in order_fields:
                if field_name not in self.ordering_fields:
                    invalid_field = True
                    break

            # If Flag, return error
            if invalid_field:
                raise serializers.ValidationError(
                    f" Invalid order field", code='500')

            # Return query after validations
            return queryset.order_by(f'{direction}{field_name}')

        return queryset
