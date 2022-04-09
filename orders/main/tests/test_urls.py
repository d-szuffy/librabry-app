from django.test import SimpleTestCase
from django.urls import resolve, reverse

from ..views import home, create_new_records_in_db, view_all_books, import_books_from_google_api


class TestUrls(SimpleTestCase):

    def test_home_url_resolvers(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)

    def test_list_url_resolvers(self):
        url = reverse("list")
        self.assertEqual(resolve(url).func, view_all_books)

    def test_create_url_resolvers(self):
        url = reverse("create")
        self.assertEqual(resolve(url).func, create_new_records_in_db)

    def test_import_url_resolvers(self):
        url = reverse("import")
        self.assertEqual(resolve(url).func, import_books_from_google_api)
