from django.urls import path
from .views import root

app_name = 'seller'

urlpatterns = [
    path('', root, name='seller'),
]