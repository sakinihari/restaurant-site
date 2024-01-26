from django.urls import path
from cart import views

urlpatterns = [
    path('cartDetails', views.cart_details, name='cartDetails'),
    path('add<int:product_id>', views.add_cart, name='add'),
    path('remove<int:product_id>', views.delete_cart, name='remove'),
    path('decrement<int:product_id>', views.min_cart, name='decrement'),


]
