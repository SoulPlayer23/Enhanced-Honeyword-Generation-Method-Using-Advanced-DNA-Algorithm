import django
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

# Create your views here.

from .models import *
from .forms import CreateUserForm

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form  = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form' : form}
    return render(request, 'authpages/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'authpages/login.html', context)

def mainPage(request):
    context = {}
    return render(request, 'authpages/main.html', context)
