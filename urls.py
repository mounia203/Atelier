from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('', views.home, name='home'),  # page d’accueil
    path('list/', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'), 
]
