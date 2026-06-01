from django.urls import path
from . import views

urlpatterns=[
    path("add", views.cart_add, name="cart_add"),
    path("cart_detailview", views.cart_detailview, name="cart_detailview"),

]