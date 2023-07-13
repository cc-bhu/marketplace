from django.urls import path

from .views import root

app_name = "home"

urlpatterns = [
    path("", root, name="root"),
]
