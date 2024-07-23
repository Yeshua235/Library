# pylint: disable=invalid-str-returned
# pylint: disable=missing-module-docstring
# pylint: disable=unused-import
# pylint: disable=relative-beyond-top-level
from django.shortcuts import render  # noqa: F401

# Create your views here.
from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    """
    A view for displaying a list of books.
    """
    model = Book
    template_name = 'book_list.html'
