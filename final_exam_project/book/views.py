from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from final_exam_project.book.forms import CreateBookForm, EditBookForm, DeleteBookForm
from final_exam_project.book.models import Book, Comment, Like
from final_exam_project.profile.models import Profile


# Create your views here.
def get_profile():
    return Profile.objects.first()


# Create your views here.

class CreateBookView(views.CreateView):
    model = Book
    form_class = CreateBookForm
    template_name = 'books/book-create.html'
    success_url = reverse_lazy('exploring_books')

    def form_valid(self, form):
        book = form.save(commit=False)
        book.user = self.request.user
        book.save()
        return super().form_valid(form)


def exploring_books(request):
    books = Book.objects.all()
    total_books = books.count()

    return render(request, 'home/exploring-books.html', {'books': books, 'total_books': total_books})


def liked_books(request):
    books = Book.objects.all()

    return render(request, 'home/books_liked.html', {'books': books})


def uploaded_books(request):
    books = Book.objects.all()

    return render(request, 'home/uploded_books.html', {'books': books})


def like_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    user = request.user


    if Like.objects.filter(book=book, user=user).exists():
        Like.objects.filter(book=book, user=user).delete()
        liked = False
    else:
        Like.objects.create(book=book, user=user)
        liked = True

    return redirect('book_details', pk=book_id)


def add_comment(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        Comment.objects.create(book=book, user=request.user, text=text)
    return redirect('book_details', pk=book_id)


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'books/book.details.html', {'book': book})


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = EditBookForm(instance=book)

    return render(request, 'books/book-edit.html', {'form': form, 'book': book})


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('index')

    form = DeleteBookForm(instance=book)
    return render(request, 'books/book-delete.html', {'form': form, 'book': book})
