from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(label="product name", max_length=100)
    price = forms.FloatField(label="product price")
    description = forms.CharField(label="product description", max_length=255)
