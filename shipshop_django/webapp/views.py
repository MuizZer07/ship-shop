from django.shortcuts import render, redirect
import requests
from shipshop_django.settings import API_ENDPOINT
from .global_variables import cart
from users.decorators import buyers_only
import random
import string
from django.contrib import messages

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
        product = product.json()
        owner = requests.get(product["owner"])
        owner = owner.json()

        product["owner_name"] = owner["username"]
        products.append(product)

    return render(request, 'webs/checkout.html', {'products': products, 'buyer': buyer})

def place_order(request, key, total, buyer, seller, products):
    payload = {
        'order_key': key,
        'total': total,
        'status': 'Pending',
        'buyer': buyer,
        'seller': seller,
        'products': products,
    }

    response = requests.post(API_ENDPOINT + '/orders/?post', data=payload)

    if response.status_code >= 300:
        messages.add_message(request, messages.ERROR, 'Error placing new order!')
    else:
        messages.add_message(request, messages.INFO, 'Successfully placed order!')

    response = response.json()
    return redirect('/')

def update_product(request, product_id, new_available_quantity):
    if new_available_quantity < 0:
        new_available_quantity = 0

    payload = {
        'available_quantity': int(new_available_quantity)
    }

    response = requests.put(API_ENDPOINT + '/products/' + product_id + '/', data=payload)
    print(response.json())
    if response.status_code >= 300:
        messages.add_message(request, messages.ERROR, 'Error updating product!')
    else:
        messages.add_message(request, messages.INFO, 'Successfully updated product!')

@buyers_only
def checkout_request(request):
    global cart
    product_ids = request.POST.getlist("product_ids")
    product_names = request.POST.getlist("product_names")
    owner_names = request.POST.getlist("owner_name")
    available = request.POST.getlist("available_quantity")
    quantity = request.POST.getlist("quantity")
    prices = request.POST.getlist("price")
    subtotals = request.POST.getlist("subtotal")
    total = request.POST.getlist("total")[0]
    buyer = requests.get(API_ENDPOINT + '/users/' + str(request.user.id)).json()["url"]
    order_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

    orders = {}
    total_prices = {}
    for product_id, quant in zip(product_ids, quantity):
        product = requests.get(API_ENDPOINT + '/products/' + str(product_id))
        product = product.json()

        if product["owner"] not in orders:
            orders[product["owner"]] = []
            total_prices[product["owner"]] = 0

        orders[product["owner"]].append(product["url"])
        total_prices[product["owner"]] += (int(quant) * float(product["price"]))
        new_available_quantity = int(product["available_quantity"]) - int(quant)
        update_product(request, product_id, new_available_quantity)

    for seller in orders:
        place_order(request, order_key, total_prices[seller], buyer, seller, orders[seller])

    cart = []
    return render(request, 'webs/complete.html')
