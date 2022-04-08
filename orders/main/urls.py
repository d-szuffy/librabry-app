from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),
    path("create/", views.create_new_records_in_db, name="create"),
    path("list/", views.view_all_books, name="list"),
    path("import/", views.import_books_from_google_api, name="import"),
]