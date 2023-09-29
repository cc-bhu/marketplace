from django import forms
from .models import Seller

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller  # or your custom User model
        fields = ['username', 'email']
        widgets ={
            "username":forms.TextInput(attrs={"class": "form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"})
            
        }

        


