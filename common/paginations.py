from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """
    Custom pagination class that extends PageNumberPagination.

    This pagination class allows you to include custom key-value pairs in the paginated response.
    You can set custom pagination keys dynamically by using the `CustomPaginationMixin` in your Views or ViewSets.

    Attributes:
        page_size: Number of objects per page. Defaults to 10.
        page_size_query_param:  Query parameter name for specifying the page size in the request.
                                Defaults to 'page_size'.
        max_page_size: Maximum number of objects per page. Defaults to 100.

    Methods:
        paginate_queryset: Overrides the parent class method to store the view instance.
        get_paginated_response: Overrides the parent class method to add custom key-value pairs to the response.
    """

    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate the queryset and store the view instance for later use.

        Args:
            queryset: The queryset to be paginated.
            request: The request object for the current HTTP request.
            view: The view instance associated with the request. Defaults to None.

        Returns:
            QuerySet: The paginated queryset.
        """

        self.view = view
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        """
        Create a paginated response with custom key-value pairs.

        Args:
            data: The paginated data to be included in the response.

        Returns:
            Response: The paginated response with custom key-value pairs.
        """

        response = super().get_paginated_response(data)

        custom_keys = self.view.get_custom_pagination_keys()
        response.data.update(custom_keys)

        return response
