from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'produit/product_list.html'
    context_object_name = 'products'
class ProductDetailView(DetailView):
    model = Product
    template_name = 'produit/product_detail.html'
    context_object_name = 'product'

def home(request):
    products = Product.objects.all()
    return render(request, 'produit/home.html', {'products': products})