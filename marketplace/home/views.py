from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

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
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'addproduct.html', {'form': form, 'img_obj': img_obj})
            
    else:
        form = ProductForm()
        return render(request, "addproduct.html", {"form": form})


def product_details(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, "product_details.html", {"product": product})
