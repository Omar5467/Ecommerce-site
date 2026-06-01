from django.urls import path
from . import views

urlpatterns=[
    path("add", views.cart_add, name="cart_add"),
    path("cart_detailview", views.cart_detailview, name="cart_detailview"),
    path("delete", views.cart_delete, name="cart_delete"),
    path("update", views.cart_update, name="cart_update"),

]