from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register',  views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('all-posts', views.all_posts, name='all-posts'),
]
