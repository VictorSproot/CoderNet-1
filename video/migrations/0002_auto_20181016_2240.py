# Generated by Django 2.1.1 on 2018-10-16 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='videos',
        ),
        migrations.AddField(
            model_name='video',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video', to='video.Course'),
        ),
    ]