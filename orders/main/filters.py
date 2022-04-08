import django_filters

from .models import ListOfBooks, Book
from django_filters import DateFilter, CharFilter


class BookFilter(django_filters.FilterSet):

    start_date = django_filters.NumberFilter(field_name="date_published", lookup_expr="gte")
    end_date = django_filters.NumberFilter(field_name="date_published", lookup_expr="lte")

    title = CharFilter(field_name="title", lookup_expr="icontains")
    author = CharFilter(field_name="author", lookup_expr="icontains")

    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['isbn_number', 'pages_number', 'edit_status', 'date_published',
                   'page_title_href', 'listofbooks']
