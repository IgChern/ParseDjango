from rest_framework.filters import OrderingFilter
from parse_app.models import Post


class CustomOrderingFilter(OrderingFilter):
    '''
    Make custom ordering class, which provide direction and order in function
    '''

    # Check the direction
    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)

        # Make field_name and direction from ordering
        field_name = ordering[0].lstrip('-')
        if ordering[0].startswith('-'):
            direction = '-'
        else:
            direction = ''

        # Set filter to queryset
        return queryset.order_by(f'{direction}{field_name}')
