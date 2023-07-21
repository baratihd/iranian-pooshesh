from .paginations import CustomPagination


class CustomPaginationMixin:
    """
    Mixin to be used with API views or viewsets to enable custom pagination.

    To use custom pagination, subclass your view or viewset from this mixin and define the
    `get_custom_pagination_keys` method to provide custom key-value pairs.

    Attributes:
        pagination_class:   The custom pagination class to be used for pagination.
                            Defaults to CustomPagination.

    Methods:
        get_custom_pagination_keys: Override this method to return custom key-value pairs for pagination.
                                    Defaults to an empty dictionary.
    """

    pagination_class = CustomPagination

    def get_custom_pagination_keys(self) -> dict:
        """
        Get custom key-value pairs for pagination.

        This method should be overridden in the view or viewset to provide custom
        key-value pairs to be included in the paginated response.

        Returns:
            dict:   A dictionary containing custom key-value pairs for the paginated response.
                    Defaults to an empty dictionary.
        """
        return {}
