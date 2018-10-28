from django.urls import path
from .views import *


urlpatterns = [
    path('', articles_list, name='articles_list_url'),
    path('<cat_name>/<slug>/', article_detail, name='article_detail_url'),
    path('<slug>/', category_detail, name='category_detail_articles_url')
]
