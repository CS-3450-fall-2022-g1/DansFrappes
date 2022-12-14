from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.view_cart, name='cart'),
    path('cart/add/', views.add_to_cart, name='cart_add'),
    path('cart/remove/<int:index>', views.remove_from_cart, name='cart_remove'),
    path('confirm/', views.view_confirm, name='confirm'),
    path('<item>/', views.view_item, name='menu_item')
]