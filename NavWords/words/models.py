from django.contrib.auth import get_user_model
from django.forms import modelformset_factory, inlineformset_factory
from django.urls import reverse
from django.utils.text import slugify
from NavWords import settings
from django.db import models


class WordList(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lists')
    slug = models.SlugField(blank=False, null=False, unique=True)

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(**kwargs)

    def get_absolute_url(self):
        return reverse('words:dictionary', kwargs={'slug': self.slug})


class Word(models.Model):
    english = models.CharField(max_length=50)
    translation = models.CharField(max_length=50)
    list = models.ForeignKey(WordList, related_name='words', on_delete=models.PROTECT)
