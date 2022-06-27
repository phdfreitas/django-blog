from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import post_save

class Post(models.Model):
    STATUS      = (('publico', 'Público'), ('privado', 'Privado'))
    titulo      = models.CharField(max_length=100)
    subtitulo   = models.CharField(max_length=100)
    slug        = models.SlugField(max_length=100)
    descricao   = models.TextField()
    autor       = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacao  = models.DateTimeField(default=timezone.now)
    atualizacao = models.DateTimeField(auto_now_add=True)
    status      = models.CharField(max_length=12, choices=STATUS, default='indisponível')

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('postDetail', args=[self.slug])

    def get_absolute_url_update(self):
        return reverse('postUpdate', args=[self.slug])

    def get_absolute_url_delete(self):
        return reverse('postDelete', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'post-by-{self.autor.username}-{self.titulo}')
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['publicacao']

