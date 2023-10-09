from django.http import HttpResponseRedirect
from django.shortcuts import render

from .form import RegistrationForm
from .models import User


# Create your views here.
# Create your views here.
def seller_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "seller_form.html", {"form": form})
    else:
        form = RegistrationForm()

    return render(request, "seller_form.html", {"form": form})
