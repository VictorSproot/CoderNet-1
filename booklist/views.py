from django.shortcuts import render
from .models import *
from .utils import *
from django.views.generic import View
from django.core.paginator import Paginator
from video.models import Course
from articles.models import Articles


# Create your views here.
def book_list(request):
    books = Book.objects.all()
    categories = Category.objects.all()

    # Пагинатор начало
    paginator = Paginator(books, 1)
    page_number = request.GET.get('page', default=1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    # Пагинатор конец

    context = {
        'books': books,
        'categories': categories,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url,
        'page_object': page,
    }
    return render(request, 'booklist/booklist.html', context=context)


class BookDetail(ObjectDetailMixin, View):
    model = Book
    template = 'booklist/book_detail.html'


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    eng_books = Book.objects.filter(lang_category=2, category=category)
    rus_books = Book.objects.filter(lang_category=1, category=category)
    books = Book.objects.filter(category=category)
    if not category:
        return render(request, 'booklist/404.html', context={})

    # Пагинатор начало
    paginator1 = Paginator(rus_books, 12)
    page_number1 = request.GET.get('page', default=1)
    page1 = paginator1.get_page(page_number1)
    is_paginated1 = page1.has_other_pages()

    if page1.has_previous():
        prev_url1 = '?page={}'.format(page1.previous_page_number())
    else:
        prev_url1 = ''

    if page1.has_next():
        next_url1 = '?page={}'.format(page1.next_page_number())
    else:
        next_url1 = ''
    # Пагинатор конец

    # Пагинатор начало
    paginator2 = Paginator(eng_books, 12)
    page_number2 = request.GET.get('page', default=1)
    page2 = paginator2.get_page(page_number2)
    is_paginated2 = page2.has_other_pages()

    if page2.has_previous():
        prev_url2 = '?page={}'.format(page2.previous_page_number())
    else:
        prev_url2 = ''

    if page2.has_next():
        next_url2 = '?page={}'.format(page2.next_page_number())
    else:
        next_url2 = ''
    # Пагинатор конец

    context = {
        'category': category,
        'categories': categories,
        'eng_books': eng_books,
        'rus_books': rus_books,
        'page_object1': page1,
        'is_paginated1': is_paginated1,
        'prev_url1': prev_url1,
        'next_url1': next_url1,
        'page_object2': page2,
        'is_paginated2': is_paginated2,
        'prev_url2': prev_url2,
        'next_url2': next_url2,
        'paginator1': paginator1,
        'paginator2': paginator2
    }
    return render(request, 'booklist/category_detail.html', context=context)


#  RSS лента
from django.contrib.syndication.views import Feed


class BookFeed(Feed):
    title = 'CoderNet Портал для помощи программистам'
    description = 'Последние опубликованные книги'
    link = '/'

    def items(self):
        qs = list(Book.objects.all()) + list(Course.objects.all()) + list(Articles.objects.all())
        print(qs)
        print()
        print(qs[1].title)
        print()
        print(qs[1].lang_category)
        return qs

    def item_title(self, item):
        return item.title
