from django.http import HttpResponseRedirect

from django.shortcuts import render
from .models import User
from .form import RegistrationForm

# Create your views here.
# Create your views here.
def seller_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'seller_form.html', {'form': form})