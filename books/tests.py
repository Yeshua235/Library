# pylint: disable=invalid-str-returned
# pylint: disable=missing-module-docstring
# pylint: disable=unused-import
# pylint: disable=relative-beyond-top-level
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from .models import Book

class BookTests(TestCase):
    """
    test for book model

    Args:
        TestCase (_type_): _description_
    """
    @classmethod
    def setUpTestData(cls):
        """
        create test data
        """
        cls.book = Book.objects.create(
            title = 'A good title',
            subtitle = 'An excellent subtitle',
            author = 'Tom Chritie',
            isbn = '1234567890123',
        )

    def test_book_content(self):
        """
        test book content
        """
        self.assertEqual(self.book.title, 'A good title')
        self.assertEqual(self.book.subtitle, 'An excellent subtitle')
        self.assertEqual(self.book.author, 'Tom Chritie')
        self.assertEqual(self.book.isbn, '1234567890123')

    def test_book_listview(self):
        """
        test for responses
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'book_list.html')
