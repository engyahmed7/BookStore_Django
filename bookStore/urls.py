from django.urls import path
from . import views

app_name = 'bookStore';

urlpatterns = [
    path('', views.get_books, name='getAll'),
    path('<int:id>', views.get_book, name='get'),
    path('add', views.create_book, name='create'),
    path('edit/<int:book_id>', views.edit_book, name="update"),
    path('delete/<int:book_id>', views.delete_book, name="delete")
]
