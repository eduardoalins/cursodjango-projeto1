from django.db import models

class Empresas(models.Model):
    nome = models.TextField(max_length = 80)
    rua = models.TextField(max_length = 300)