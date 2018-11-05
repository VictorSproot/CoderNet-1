"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import main_page, search_books, search_articles, search_courses

from django.contrib.sitemaps.views import sitemap
from books.sitemaps import *

from booklist.views import BookFeed

sitemaps = {
    'articles_category': ArticlesCategorySitemap,
    'video_category': VideoCategorySitemap,
    'books_category': BookCategorySitemap,
    'books': BookSitemap,
    'courses': CourseSitemap,
    'articles': ArticleSitemap,
    'static': StaticViewSitemap
}

urlpatterns = [
    path('rss.xml', BookFeed(), name='book_rss_url'),
    path('admin/', admin.site.urls),
    path('search_books/', search_books, name='search_books_url'),
    path('search_articles/', search_articles, name='search_articles_url'),
    path('search_courses/', search_courses, name='search_courses_url'),
    path('', main_page, name='main_page_url'),
    path('books/', include('booklist.urls')),
    path('videos/', include('video.urls')),
    path('articles/', include('articles.urls')),
    path('sitemaps.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
