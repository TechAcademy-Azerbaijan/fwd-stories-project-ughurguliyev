from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    surname = models.CharField(max_length=100, verbose_name="Surname")
    username = models.CharField(max_length=60, verbose_name="Username", unique=True)
    email = models.EmailField(verbose_name="Email")
    password = models.CharField(max_length=300)



    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    
    def __str__(self):
        return self.username
