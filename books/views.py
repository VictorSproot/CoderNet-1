from django.shortcuts import render, redirect
from video.models import Course
from articles.models import Articles
from booklist.models import Book


def main_page(request):
    return render(request, 'booklist/home.html')


def search_books(request):
    search_query = request.GET.get('search', '')
    if search_query:
        books = Book.objects.filter(title__icontains=search_query)
        if books:
            context = {
                'books': books,
            }
            return render(request, 'booklist/search_books.html', context=context)
        else:
            return render(request, 'booklist/search.html')  # По вашему запросу ничего не найдено
    else:
        return render(request, 'booklist/404.html')  # Вы ввели пустой запрос


def search_courses(request):
    search_query = request.GET.get('search', '')
    if search_query:
        courses = Course.objects.filter(title__icontains=search_query)
        if courses:
            context = {
                'courses': courses,
            }
            return render(request, 'booklist/search_courses.html', context=context)
        else:
            return render(request, 'booklist/search.html')  # По вашему запросу ничего не найдено
    else:
        return render(request, 'booklist/404.html')  # Вы ввели пустой запрос


def search_articles(request):
    search_query = request.GET.get('search', '')
    if search_query:
        articles = Articles.objects.filter(title__icontains=search_query)
        if articles:
            context = {
                'articles': articles
            }
            return render(request, 'booklist/search_articles.html', context=context)
        else:
            return render(request, 'booklist/search.html')  # По вашему запросу ничего не найдено
    else:
        return render(request, 'booklist/404.html')  # Вы ввели пустой запрос
