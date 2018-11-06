from django.shortcuts import render, redirect
from video.models import Course
from articles.models import Articles
from booklist.models import Book

from django.shortcuts import render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View


def main_page(request):
    return render(request, 'booklist/home.html')


class SearchView(View):
    template_name = 'booklist/search_new.html'

    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('search')
        if question is not None:
            books = Book.objects.filter(title__icontains=question)
            courses = Course.objects.filter(title__icontains=question)
            articles = Articles.objects.filter(title__icontains=question)
            objects = list(books) + list(courses) + list(articles)

            context['last_question'] = '?search=%s' % question

            current_page = Paginator(objects, 10)

            page = request.GET.get('page')
            try:
                context['objects'] = current_page.page(page)
            except PageNotAnInteger:
                context['objects'] = current_page.page(1)
            except EmptyPage:
                context['objects'] = current_page.page(current_page.num_pages)
        return render_to_response(template_name=self.template_name, context=context)


#  RSS лента
from django.contrib.syndication.views import Feed


class Rss(Feed):
    title = 'CoderNet Портал для помощи программистам'
    description = 'Последние опубликованные книги'
    link = '/'

    def items(self):
        qs = list(Book.objects.all()) + list(Course.objects.all()) + list(Articles.objects.all())
        return qs

    def item_title(self, item):
        return item.title
