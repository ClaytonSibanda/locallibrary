from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
# Create your views here.

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book


def index(request):
    """view function for the home page for the iste"""
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres_with_a = Genre.objects.filter(name__contains="fiction").count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        "num_genres_with_a":num_genres_with_a,
    }
    return render(request,'index.html',context=context)


