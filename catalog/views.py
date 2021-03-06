from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
# Create your views here.

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model =Author
    paginate_by=10

class AuthorDetailView(generic.DetailView):
    model=Author
def index(request):
    """view function for the home page for the iste"""
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres_with_a = Genre.objects.filter(name__contains="fiction").count()
    num_visits = request.session.get('num_visits',0)#get session value, if not available then set a value of 0 for it.
    request.session['num_visits'] = num_visits+1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        "num_genres_with_a":num_genres_with_a,
        'num_visits':num_visits,
    }
    return render(request,'index.html',context=context)


