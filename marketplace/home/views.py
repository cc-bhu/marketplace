from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .form import ProductForm
from .models import Product


# Create your views here.
def root(request):
    return render(request, "index.html")


def products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def addproduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ProductForm()
        return render(request, "addproduct.html", {"form": form})

def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    
    return render(request, 'product_details.html', {'product': product})