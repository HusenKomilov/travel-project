from rest_framework import pagination


class RecentlyPagination(pagination.LimitOffsetPagination):
    default_limit = 7
    max_limit = 7
