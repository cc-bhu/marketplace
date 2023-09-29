from django.shortcuts import render
from .models import Seller
from .form import SellerForm

# Create your views here.
# Create your views here.
def seller_registration(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'registration/success.html')
    else:
        form = SellerForm()
    
    return render(request, 'seller/seller_registration.html', {'form': form})