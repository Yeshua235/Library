# pylint: disable=invalid-str-returned
# pylint: disable=missing-module-docstring
# pylint: disable=unused-import
# pylint: disable=relative-beyond-top-level
from django.urls import path  # noqa: F401
from .views import BookListView  # noqa: F401

urlpatterns = [
    # Add your URL patterns here
    path('', BookListView.as_view(), name='home'),
]
