from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from .models import User

def seller_profile(request):
    return render(request, 'pages/seller_profile.html')

def buyer_profile(request):
    return render(request, 'pages/buyer_profile.html')
