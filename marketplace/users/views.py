from django.http import HttpResponseRedirect
from django.shortcuts import render

from .form import RegistrationForm


def seller_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    form = RegistrationForm()
    return render(request, "seller_form.html", {"form": form})
