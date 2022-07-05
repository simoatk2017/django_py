from django.shortcuts import render
from .filter import BookFilterExp1


# Create your views here.
def filter_example_1(request):
    books = BookFilterExp1(request.GET)
    ctx = {
        "books": books
    }

    path = 'filter_app/filter_listing.html'

    return render(request, path, ctx)
