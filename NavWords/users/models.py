from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
import os


def upload_image_file(instance, filename):
    extra_context = datetime.date.today().strftime("%Y%m%d")
    name, ext = os.path.splitext(filename)
    correct_filename = f'{name}_{extra_context}{ext}'
    return f'avatar/{instance.username}/{correct_filename}'


# Установить дефолтную картинку
class User(AbstractUser):
    photo = models.ImageField(upload_to=upload_image_file, blank=True, null=True, verbose_name='profile_image')
