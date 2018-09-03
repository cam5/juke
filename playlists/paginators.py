from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination


# pylint: disable=too-few-public-methods
class LimitPagination(MultipleModelLimitOffsetPagination):
    """A pagniation class meant to mirror the configure pagination strategy for
    DRF, but matching the MultipleModel view"""
    default_limit = 2
