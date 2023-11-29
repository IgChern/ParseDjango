from rest_framework.pagination import LimitOffsetPagination


# Make new class and set new settings
class CustomPag(LimitOffsetPagination):
    '''
    This СustomPag changes methods (get_limit and get_offset)
    to provide new settings for limit and offset parameters.
    '''

    def get_limit(self, request):
        '''
        Change limit parameter by default = 5 if the limit is None or
        limit > 30 or limit <= 0.
        '''
        limit = super().get_limit(request)
        if limit is None or limit > 30 or limit <= 0:
            limit = 5
        return limit

    def get_offset(self, request):
        '''
        Change offset parameter by default = 0 if the offset in None or
        offset < 0.
        '''
        offset = super().get_offset(request)
        if offset is None or offset < 0:
            offset = 0
        return offset
