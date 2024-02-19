from rest_framework.pagination import LimitOffsetPagination


class CustomPageNumberPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 100

