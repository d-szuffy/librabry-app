from django.test import TestCase, Client
from django.urls import reverse
from ..models import ListOfBooks, Book


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.create_new_records_url = reverse('create')
        self.view_all_books_url = reverse('list')
        self.import_books = reverse('import')
        self.list_of_books_1 = ListOfBooks.objects.create(
            name="TestList"
        )

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')

    def test_create_new_records_in_db_GET(self):
        response = self.client.get(self.create_new_records_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/create.html')

    def test_view_all_books_GET(self):
        response = self.client.get(self.view_all_books_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/books.html')

    def test_import_books_from_google_api_all_books_GET(self):
        response = self.client.get(self.import_books)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/google_api.html')