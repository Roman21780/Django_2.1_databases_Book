from django.shortcuts import render
from datetime import datetime

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    context = {
        'books': books
    }
    return render(request, template, context)

def books_by_date_view(request, pub_date):
    template = 'books/books_by_date.html'

    # Преобразуем строку даты в объект date
    current_date = datetime.strptime(pub_date, '%Y-%m-%d').date()

    # Получаем книги для указанной даты
    books = Book.objects.filter(pub_date=current_date)

    # Получаем предыдущую и следующую даты
    prev_date = Book.objects.filter(pub_date__lt=current_date).order_by('-pub_date').values('pub_date').first()
    next_date = Book.objects.filter(pub_date__gt=current_date).order_by('pub_date').values('pub_date').first()

    context = {
        'books': books,
        'current_date': current_date,
        'prev_date': prev_date['pub_date'] if prev_date else None,
        'next_date': next_date['pub_date'] if next_date else None,
    }
    return render(request, template, context)
