from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class ListOfBooks(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):

    listofbooks = models.ForeignKey(ListOfBooks, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date_published = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)])
    isbn_number = models.CharField(max_length=50)
    pages_number = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)])
    page_title_href = models.URLField(max_length=1000)
    language_published = models.CharField(max_length=100)

    edit_status = models.BooleanField(null=True)

    def __str__(self):
        return self.title
