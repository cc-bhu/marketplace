# seller/urls.py
from django.urls import path

from .views import seller_registration

app_name = "users"  # Set the app_name


urlpatterns = [
    path("seller_registration", seller_registration, name="seller_registration"),
]
