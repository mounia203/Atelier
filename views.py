from django.shortcuts import redirect, get_object_or_404
from django.views import View
from produit.models import Product
from .models import Cart, CartItem
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import OrderForm
from django.views.generic import DeleteView
class AddToCartView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if created:
            cart_item.quantity = 1
        else:
            cart_item.quantity += 1
        cart_item.save()
        return redirect('cart_detail')



class CartDetailsView(DetailView):
    model = Cart
    template_name = 'orders/detail_cart.html'

    def get_object(self):
        return Cart.objects.get(user=self.request.user)



class CreateOrderView(CreateView):
    form_class = OrderForm
    template_name = 'orders/shipping.html'
    success_url = reverse_lazy('confirmation')

class CartItemDeleteView(DeleteView):
    model = CartItem
    template_name = 'orders/cartitem_delete.html'
    success_url = reverse_lazy('cart_detail')
