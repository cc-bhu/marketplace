from django.urls import path

from .form import ProductForm
from .views import addproduct, root

app_name = "home"

urlpatterns = [
    path("", root, name="root"),
    path("addproduct", addproduct, name="addproduct"),
]
