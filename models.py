from django.db import models
from users.models import CustomUser as Utilisateur


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, max_length=150)

    def __str__(self):
        return self.name 
    
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




