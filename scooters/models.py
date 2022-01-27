from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,db_index = True)
    slug = models.SlugField(max_length=200,db_index = True, unique=True)

    class Meta:
        ordering =['-name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.name}'

class Scooter(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,default='IT')
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['-created']
    