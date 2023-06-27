from rest_framework.pagination import PageNumberPagination

class SmallNumberPagination(PageNumberPagination): 
    page_size=5

class LargeNumberPagination(PageNumberPagination):
    page_size=25