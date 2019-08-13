from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from .models import User
from .decorators import sellers_only, buyers_only
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    if request.user.is_buyer:
        return buyer_dashboard(request)
    if request.user.is_seller:
        return seller_dashboard(request)

@buyers_only
def buyer_dashboard(request):
    return render(request, 'pages/buyer_dashboard.html')

@sellers_only
def seller_dashboard(request):
    return render(request, 'pages/seller_dashboard.html')
