from django.shortcuts import render, redirect
import requests
from shipshop_django.settings import API_ENDPOINT
from .global_variables import cart
from users.decorators import buyers_only

'''
    Frontend,
    view class for all web pages,
    all requests and responses from REST API endpoint,
    no direct database manipulation
'''

def index(request):
    global cart
    products = requests.get(API_ENDPOINT + '/products')
    products = products.json()

    return render(request, 'webs/index.html', {'products': products, 'cart': cart})

def about(request):
    return render(request, 'webs/about.html')

def contact(request):
    return render(request, 'webs/contact.html')

def add_to_cart(request, product_id):
    global cart
    if product_id not in cart:
        cart.append(int(product_id))

    return redirect('/')

def remove_from_cart(request, product_id):
    global cart
    if int(product_id) in cart:
        cart.remove(int(product_id))

    return redirect('/')

def clear_cart(request):
    global cart
    cart = []

    return redirect('/')

@buyers_only
def checkout(request):
    global cart
    buyer = request.user.id
    products = []

    for product_id in cart:
        product =  requests.get(API_ENDPOINT + '/products/' + str(product_id))
        products.append(product.json())

    return render(request, 'webs/checkout.html', {'products': products, 'buyer': buyer})

@buyers_only
def checkout_request(request):
    pass
