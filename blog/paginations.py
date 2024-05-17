from rest_framework import pagination


class BlogPagination(pagination.LimitOffsetPagination):
    default_limit = 9
    max_limit = 9

