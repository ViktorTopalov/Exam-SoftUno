from django import forms
from .models import Book

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author',  'publication_date', 'genre','price', 'description','picture']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
            'picture': forms.TextInput(attrs={'placeholder': 'https://...'}),

        }



class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author',  'publication_date', 'genre','price', 'description','picture']

class DeleteBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author',  'publication_date', 'genre','price', 'description','picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True


