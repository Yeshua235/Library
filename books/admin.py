# pylint: disable=relative-beyond-top-level
# pylint: disable=missing-module-docstring
from django.contrib import admin

# Register your models here.
from .models import Book

admin.site.register(Book)
