from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import LoginForm


def home(request):
    return render(request, 'home.html')


# def login(request):
#     return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


def all_posts(request):
    return render(request, 'all-posts.html')


class CustomLoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('register')
