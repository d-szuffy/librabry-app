from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .filters import BookFilter
from .forms import CreateNewBook

from .common.util.google_books_api import *

# Create your views here.


def home(response):
    return render(response, 'main/home.html', {})


def create_new_records_in_db(response):
    ls = ListOfBooks.objects.get(id=1)
    form = CreateNewBook()

    if response.method == "POST":

        if response.POST.get("newItem"):
            form = CreateNewBook(response.POST)
            if form.is_valid():

                ttl = form.cleaned_data["title"]
                author = form.cleaned_data["author"]
                date_pub = form.cleaned_data["date_published"]
                isbn = form.cleaned_data["isbn_number"]
                pages_no = form.cleaned_data["pages_number"]
                link = form.cleaned_data["page_title_href"]
                lang = form.cleaned_data["language_published"]

                book = Book(listofbooks=ls, title=ttl, author=author, date_published=date_pub, isbn_number=isbn,
                            pages_number=pages_no, page_title_href=link, language_published=lang)
                book.save()

        elif response.POST.get("clearList"):
            for item in ls.book_set.all():

                item.delete()

        for item in ls.book_set.all():
            if response.POST.get("editItem" + str(item.id)):
                item.edit_status = True
                item.save()

            elif response.POST.get("submitItemChanges" + str(item.id)):
                new_ttl = response.POST.get("editTitle" + str(item.id))
                item.title = new_ttl
                item.edit_status = False
                item.save()

    return render(response, 'main/create.html', {"form": form, "ls": ls})


def view_all_books(response):

    ls = ListOfBooks.objects.get(id=1)

    books = ls.book_set.all()

    my_filter = BookFilter(response.GET, queryset=books)
    books = my_filter.qs

    return render(response, 'main/books.html', {"ls": ls, "books": books, "myFilter": my_filter})


def import_books_from_google_api(response):

    ls = ListOfBooks.objects.get(id=1)

    if response.method == "POST":

        if response.POST.get("importBooks"):

            key_word = response.POST.get("keyWord")

            books_from_api_json = get_books_from_google_api_filter_with_provided_key_word({"q": key_word})

            books_from_google_api = GoogleBook(books_from_api_json,
                                               ["title", "authors", "publishedDate", "industryIdentifiers", "pageCount",
                                                "imageLinks",
                                                "language"]
                                               )
            books_from_google_api.fill_missing_keys_in_response_with_default_value()
            books_from_google_api.get_books_info_final_forms_from_raws_gathered_form_json()

            for title, author, date, isbn, count, link, lang in zip(books_from_google_api.books_titles,
                                                                    books_from_google_api.books_authors,
                                                                    books_from_google_api.books_publication_dates,
                                                                    books_from_google_api.books_isbn,
                                                                    books_from_google_api.books_page_count,
                                                                    books_from_google_api.books_image_links,
                                                                    books_from_google_api.books_languages):
                ttl = title
                auth = author[0]
                try:
                    date = str(date)[0:4]
                    date_pub = int(date)
                except ValueError or IndexError:
                    date_pub = 0
                if type(isbn) == str:
                    isbn_ = " - "
                else:
                    isbn_ = isbn[0]["type"]

                if type(count) == str:
                    pages_no = 0
                else:
                    pages_no = count
                if type(link) == str:
                    img_link = " - "
                else:
                    img_link = link["thumbnail"]

                pub_lang = lang

                ls.book_set.create(title=ttl, author=auth, date_published=date_pub, isbn_number=isbn_,
                                   pages_number=pages_no, page_title_href=img_link, language_published=pub_lang)

    return render(response, 'main/google_api.html', {})
