from django.urls import path

from .form import ProductForm
from .views import addproduct, products, root,product_details

app_name = "home"

urlpatterns = [
    path("", root, name="root"),
    path("addproduct", addproduct, name="addproduct"),
    path("products", products, name="products"),
    path('products/<uuid:id>', product_details, name='product_details'),
]
