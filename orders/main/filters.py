import django_filters

from .models import ListOfBooks, Book
from django_filters import DateFilter, CharFilter
from django.forms.widgets import TextInput


class BookFilter(django_filters.FilterSet):

    start_date = django_filters.NumberFilter(field_name="date_published", lookup_expr="gte", label="", widget=TextInput(attrs={'placeholder': 'Date from'}))
    end_date = django_filters.NumberFilter(field_name="date_published", lookup_expr="lte", label="", widget=TextInput(attrs={'placeholder': 'Date to'}))

    title = CharFilter(field_name="title", lookup_expr="icontains", label="", widget=TextInput(attrs={'placeholder': 'Title contains'}))
    author = CharFilter(field_name="author", lookup_expr="icontains", label="", widget=TextInput(attrs={'placeholder': 'Author contains'}))
    language_published = CharFilter(field_name="language_published", lookup_expr="icontains", label="", widget=TextInput(attrs={'placeholder': 'Language'}))

    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['isbn_number', 'pages_number', 'edit_status', 'date_published',
                   'page_title_href', 'listofbooks']
