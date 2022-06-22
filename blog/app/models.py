from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS      = (('disponível', 'Disponível'), ('indisponível', 'Indisponível'))
    titulo      = models.CharField(max_length=100)
    slug        = models.SlugField(max_length=100)
    descricao   = models.TextField()
    autor       = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacao  = models.DateTimeField(default=timezone.now)
    atualizacao = models.DateTimeField(auto_now_add=True)
    status      = models.CharField(max_length=12, choices=STATUS, default='indisponível')

    def __str__(self) -> str:
        return self.titulo 