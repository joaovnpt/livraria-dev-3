from django.db import models

class Caetgoria(models.Model):
    descricao = models.CharField(max_length=100)