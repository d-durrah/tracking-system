from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created successfully')
            return redirect('accounts:login')
    else:
        form = UserForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_request(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('frontend:index'))
    return render(request=request, template_name="accounts/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('frontend:index')