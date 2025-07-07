from rest_framework.pagination import CursorPagination
from rest_framework.response import Response


class CustomResultsSetPagination(CursorPagination):
    page_size = 20
    max_page_size = 20
    ordering = "id"

    def get_paginated_response(self, data):
        return Response(
            {
                "next": self.get_next_link(),
                "results": data,
            }
        )
