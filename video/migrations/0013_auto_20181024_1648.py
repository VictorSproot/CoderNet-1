# Generated by Django 2.1.2 on 2018-10-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0012_auto_20181022_1228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-created'], 'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AddField(
            model_name='course',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
