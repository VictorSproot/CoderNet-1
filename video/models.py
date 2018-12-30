from django.db import models
from django.shortcuts import reverse

from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


def generate_filename_jpg(instance, filename):
    filename = instance.slug + '.jpg'
    return "{0}/{1}".format(instance, filename)


def generate_filename_jpg_video(instance, filename):
    filename = instance.title + '.jpg'
    return "{0}/{1}".format(instance, filename)


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200, db_index=True, blank=True, verbose_name='Название')
    link = models.CharField(max_length=500, verbose_name='Ссылка на видео')
    course = models.ForeignKey('Course', related_name='video', on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name='Курс')

    def __str__(self):
        return self.title

    def generate_file_preview(self):
        return "https://img.youtube.com/vi/{}/hqdefault.jpg".format(self.link.split('.')[2].split('=')[1])

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Course(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Название курса')
    slug = models.SlugField(max_length=200, verbose_name='Ссылка', unique=True)
    description = RichTextField(blank=True, db_index=True, verbose_name='Описание')
    desc_for_find = models.TextField(blank=True, db_index=True, verbose_name='Описание для поиска')
    keywords = models.CharField(max_length=200, blank=True, verbose_name='Кейвордс')
    category = models.ManyToManyField('Category', related_name='courses', verbose_name='Категория')
    img_file = models.ImageField(upload_to=generate_filename_jpg, null=True, blank=True, verbose_name='IMG')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def get_model_name(self):
        return 'Курс'

    def get_absolute_url(self):
        cat_name = self.category.first().slug
        return reverse('course_detail_url', kwargs={'slug': self.slug, 'cat_name': cat_name})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'
        ordering = ['-created']


class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Название категории', blank=True)
    slug = models.SlugField(max_length=200, verbose_name='Ссылка')
    desc_for_find = models.TextField(blank=True, db_index=True, verbose_name='Описание для поиска')
    keywords = models.CharField(max_length=200, blank=True, verbose_name='Кейвордс')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_video_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Comments(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    comment_author_course = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='comments_course')
    comment_text = models.TextField(verbose_name='Добавить комментарий')
    comment_article = models.ForeignKey(Course, on_delete=models.CASCADE)
    comment_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Author --> {}; course --> {}; text --> {}'.format(self.comment_author_course, self.comment_article, self.comment_text)
