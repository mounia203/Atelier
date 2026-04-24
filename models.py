from django.db import models
from users.models import CustomUser as Utilisateur
from produit.models import Product, Category


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class CartItem(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class OrderTable(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField()
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class OrderItem(models.Model):
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(OrderTable, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
