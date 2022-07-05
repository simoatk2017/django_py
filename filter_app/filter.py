import django_filters
from .models import Book, Author


class BookFilterExp1(django_filters.FilterSet):
    # book_name = django_filters.CharFilter(lookup_expr='iexact')
    book_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['status']
