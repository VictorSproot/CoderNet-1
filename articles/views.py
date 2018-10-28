from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


# Create your views here.
def articles_list(request):
    articles = Articles.objects.all()
    categories = Category.objects.all()

    # Пагинатор начало
    paginator = Paginator(articles, 1)
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
        'articles': articles,
        'categories': categories,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url,
        'page_object': page,
    }
    return render(request, 'articles/article_list.html', context=context)


def article_detail(request, **kwargs):
    article = Articles.objects.get(slug__iexact=kwargs['slug'])
    categories = Category.objects.all()
    context = {
        'article': article,
        'categories': categories
    }
    return render(request, 'articles/article_detail.html', context=context)


def category_detail(request, slug):
    category = Category.objects.get(slug__iexact=slug)
    categories = Category.objects.all()
    articles = Articles.objects.filter(category=category)

    # Пагинатор начало
    paginator = Paginator(articles, 12)
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
        'category': category,
        'categories': categories,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url,
        'page_object': page,
        'articles': articles
    }
    return render(request, 'articles/category_list.html', context=context)
