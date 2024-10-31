from django.urls import path
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('register',  register, name='register'),
    path('login', login, name='login'),
]
