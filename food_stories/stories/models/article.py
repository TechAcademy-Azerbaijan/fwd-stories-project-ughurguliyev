from django.db import models

from .author import Author
from .category import Category

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.CharField(max_length=50 ,verbose_name="Short description")
    body = models.TextField(verbose_name="Body")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name= 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title