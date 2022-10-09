from django.urls import path
from . import views

urlpatterns = [
    path('details/',views.cart_details,name='cartDetails'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('decr/<int:product_id>/', views.min_cart, name='decrement'),
    path('del/<int:product_id>/', views.cart_delete, name='remove'),
]
