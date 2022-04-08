import requests
import json
from dataclasses import dataclass


def get_books_from_google_api_filter_with_provided_key_word(params):

    URL = "https://www.googleapis.com/books/v1/volumes"
    r = requests.get(url=URL, params=params)
    data = r.text
    data_json = json.loads(data)

    return data_json


def get_books_info_from_json_response(data_json, info_type):
    books_info = []
    for item in data_json["items"]:

        try:
            books_info.append(item["volumeInfo"][info_type])
        except KeyError:
            books_info.append("")

    return books_info


@dataclass(init=True)
class GoogleBook:

    books_from_api_json: dict

    keys_which_interest_me: list = None

    prepared_data_to_add_to_database: list = None

    books_titles: list = None
    books_authors: list = None
    books_publication_dates: list = None
    books_isbn: list = None
    books_page_count: list = None
    books_image_links: list = None
    books_languages: list = None

    def fill_missing_keys_in_response_with_default_value(self):
        keys_which_interest_me = ["title", "authors", "publishedDate", "industryIdentifiers", "pageCount", "imageLinks",
                                  "language"]

        for item in self.books_from_api_json["items"]:
            for key in keys_which_interest_me:
                if key not in item["volumeInfo"]:
                    item["volumeInfo"][key] = " - "

    def get_books_info_final_forms_from_raws_gathered_form_json(self):

        self.books_titles = get_books_info_from_json_response(self.books_from_api_json, "title")
        self.books_authors = get_books_info_from_json_response(self.books_from_api_json, "authors")
        self.books_publication_dates = get_books_info_from_json_response(self.books_from_api_json, "publishedDate")
        self.books_isbn = get_books_info_from_json_response(self.books_from_api_json, "industryIdentifiers")
        self.books_page_count = get_books_info_from_json_response(self.books_from_api_json, "pageCount")
        self.books_image_links = get_books_info_from_json_response(self.books_from_api_json, "imageLinks")
        self.books_languages = get_books_info_from_json_response(self.books_from_api_json, "language")

    def prepare_data_for_database_format(self):

        for item in self.books_from_api_json["items"]:
            pass

