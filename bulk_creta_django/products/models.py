from django.db import models


class Product(models.Model):
    name = models.CharField('Nome produto', max_length=50)
