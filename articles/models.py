from django.db import models
from django.shortcuts import reverse

from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


# Create your models here.

def generate_filename_jpg(instance, filename):
    filename = instance.slug + '.jpg'
    return "{0}/{1}".format(instance, filename)


class Articles(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='Название статьи')
    slug = models.SlugField(max_length=300, verbose_name='Ссылка', unique=True)
    body = RichTextField(blank=True, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True)
    desc_for_find = models.TextField(blank=True, db_index=True, verbose_name='Описание для поиска')
    keywords = models.CharField(max_length=200, blank=True, verbose_name='Кейвордс')
    category = models.ManyToManyField('Category', related_name='articles', verbose_name='Категория', blank=True)
    img_file = models.ImageField(upload_to=generate_filename_jpg, null=True, blank=True, verbose_name='IMG')

    def get_model_name(self):
        return 'Статья'

    def get_absolute_url(self):
        cat_name = self.category.first().slug
        return reverse('article_detail_url', kwargs={'slug': self.slug, 'cat_name': cat_name})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created']


class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=200, verbose_name='Ссылка', unique=True)
    desc_for_find = models.TextField(blank=True, db_index=True, verbose_name='Описание для поиска')
    keywords = models.CharField(max_length=200, blank=True, verbose_name='Кейвордс')

    def get_absolute_url(self):
        return reverse('category_detail_articles_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['title']

class Comments(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    comment_text = models.TextField(verbose_name='Добавить комментарий')
    comment_article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    comment_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Author --> {}; post --> {}; text --> {}'.format(self.comment_author, self.comment_article, self.comment_text)
