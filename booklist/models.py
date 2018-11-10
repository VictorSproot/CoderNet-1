from django.db import models
from django.shortcuts import reverse

from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

CATEGORIES = (
    (1, 'Русский'),
    (2, 'Английский')
)


def generate_filename(instance, filename):
    filename = instance.slug + '.pdf'
    return "{0}/{1}".format(instance, filename)


def generate_filename_jpg(instance, filename):
    filename = instance.slug + '.jpg'
    return "{0}/{1}".format(instance, filename)


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Ссылка')
    description = RichTextField(blank=True, db_index=True, verbose_name='Описание')
    desc_for_find = models.TextField(blank=True, db_index=True, verbose_name='Описание для поиска')
    keywords = models.CharField(max_length=200, blank=True, verbose_name='Кейвордс')
    category = models.ManyToManyField('Category', related_name='books', verbose_name='Категория')
    lang_category = models.IntegerField(choices=CATEGORIES, default=1, db_index=True, verbose_name='Язык')
    book_file = models.FileField(upload_to=generate_filename, null=True, blank=True, verbose_name='Файл PDF')
    img_file = models.ImageField(upload_to=generate_filename_jpg, null=True, blank=True, verbose_name='IMG')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def get_model_name(self):
        return 'Книга'

    def get_absolute_url(self):
        cat_name = self.category.first().slug
        return reverse('book_detail_url', kwargs={'slug': self.slug, 'cat_name': cat_name})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-created']

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    desc_for_find_cat = models.TextField(blank=True, db_index=True, verbose_name='Описание для поиска')
    keywords_cat = models.CharField(max_length=200, blank=True, verbose_name='Кейвордс')

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title


class Comments(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    comment_author_book = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='comments_book')
    comment_text = models.TextField(verbose_name='Добавить комментарий')
    comment_article = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Author --> {}; book --> {}; text --> {}'.format(self.comment_author_book, self.comment_article, self.comment_text)