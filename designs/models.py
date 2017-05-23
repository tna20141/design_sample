from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Product(models.Model):
    description = models.TextField()
    owner = models.CharField(max_length=40)
    path = models.CharField(max_length=100)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.path
