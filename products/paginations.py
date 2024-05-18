from rest_framework.pagination import LimitOffsetPagination


class ProductListPagination(LimitOffsetPagination):
    default_limit = 9
    max_limit = 9
