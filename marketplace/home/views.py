from django.http import HttpResponseRedirect
from django.shortcuts import render

from .form import ProductForm


# Create your views here.
def root(request):
    return render(request, "index.html")


def addproduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ProductForm()
        return render(request, "addproduct.html", {"form": form})
