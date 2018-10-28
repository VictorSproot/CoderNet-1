# Generated by Django 2.1.1 on 2018-10-16 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20181016_2244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ссылка'),
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Название категории'),
        ),
    ]
