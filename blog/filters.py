import django_filters
from .models import Blog

'''
https://www.codechit.com/django-filter-search-form-guide/
'''


class BlogFilter(django_filters.FilterSet):
    '''
      xcc
    '''
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Blog
        fields = ['title', 'categories']
