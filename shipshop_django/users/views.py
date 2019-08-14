from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from .models import User
from .decorators import sellers_only, buyers_only
from django.contrib.auth.decorators import login_required
import requests
from shipshop_django.settings import API_ENDPOINT

@login_required
def profile(request, user_id):
    user = requests.get(API_ENDPOINT + '/users/' + str(user_id)).json()
    return render(request, 'pages/profile.html', {'user': user})

@login_required
def dashboard(request):
    if request.user.is_buyer:
        return buyer_dashboard(request)
    if request.user.is_seller:
        return seller_dashboard(request)

@buyers_only
def buyer_dashboard(request):
    orders = requests.get(API_ENDPOINT + '/orders/').json()

    my_orders = []
    for order in orders:
        buyer = requests.get(order["buyer"]).json()
        if buyer["id"] == request.user.id:
            my_orders.append(order)

    return render(request, 'pages/buyer_dashboard.html', {'orders': my_orders})

@sellers_only
def seller_dashboard(request):
    orders = requests.get(API_ENDPOINT + '/orders/').json()

    my_orders = []
    for order in orders:
        seller = requests.get(order["seller"]).json()
        if seller["id"] == request.user.id:
            my_orders.append(order)

    return render(request, 'pages/seller_dashboard.html', {'orders': my_orders})
