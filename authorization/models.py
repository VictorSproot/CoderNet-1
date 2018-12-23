from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def generate_filename_jpg(instance, filename):
    filename = str(instance.pk) + '.jpg'
    return "{0}/{1}".format(instance, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=generate_filename_jpg, null=True, blank=True, verbose_name='Аватарка')
    city = models.CharField(max_length=200, blank=True, verbose_name='Город')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
