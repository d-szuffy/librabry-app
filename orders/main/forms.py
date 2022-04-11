from django import forms
from django.forms import TextInput
from django.core.validators import MaxValueValidator, MinValueValidator


class CreateNewBook(forms.Form):

    title = forms.CharField(max_length=200, required=True, label="", widget=TextInput(attrs={'placeholder': 'Title'}))
    author = forms.CharField(max_length=200, required=True, label="", widget=TextInput(attrs={'placeholder': 'Author'}))
    date_published = forms.IntegerField(required=True, min_value=0, max_value=10000, label="",
                                        widget=TextInput(attrs={'placeholder': 'Publication Year'}),
                                        error_messages={"min_value": "Year publication must be a positive integer."})
    isbn_number = forms.CharField(required=True, max_length=50, label="", widget=TextInput(attrs={'placeholder': 'ISBN'}))
    pages_number = forms.IntegerField(required=True, min_value=0, max_value=10000, label="",
                                      widget=TextInput(attrs={'placeholder': 'Pages number'}),
                                      error_messages={"min_value": "Year publication must be a positive integer."})
    page_title_href = forms.URLField(required=True, max_length=1000, label="", widget=TextInput(attrs={'placeholder': 'Title Page Link'}))
    language_published = forms.CharField(required=True, max_length=100, label="", widget=TextInput(attrs={'placeholder': 'Language'}))
