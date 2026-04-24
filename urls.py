from django.urls import path
from .views import AddToCartView, CartDetailsView, CartItemDeleteView, CreateOrderView

urlpatterns = [
    path('add/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartDetailsView.as_view(), name='cart_detail'),
    path('delete/<int:pk>/', CartItemDeleteView.as_view(), name='cartitem_delete'),
     path('shipping/', CreateOrderView.as_view(), name='create_order'),
]
