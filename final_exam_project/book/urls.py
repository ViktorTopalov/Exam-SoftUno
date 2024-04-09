from django.urls import path, include

from final_exam_project.book.views import CreateBookView, delete_book, edit_book, book_details, exploring_books, \
    like_book, add_comment, liked_books, uploaded_books

urlpatterns = (
    path('uploaded_books/',uploaded_books,name='uploaded_books'),
    path('liked_books/',liked_books, name='liked_books'),
    path('like/<int:book_id>/', like_book, name='like_book'),
    path('comment/<int:book_id>/', add_comment, name='add_comment'),
    path('create/',CreateBookView.as_view(),name='create_book'),
    path('exploring-books/',exploring_books,name='exploring_books'),
    path('<int:pk>/',include([
        path('details/',book_details,name='book_details'),
        path('edit/',edit_book,name='edit_book'),
        path('delete/',delete_book,name='delete_book')
        ])
))