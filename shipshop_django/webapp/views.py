from django.shortcuts import render, redirect
import requests
from shipshop_django.settings import API_ENDPOINT
from .global_variables import cart
from users.decorators import buyers_only
import random
import string
from django.contrib import messages
from django.http import HttpResponseRedirect

'''
    Frontend,
    view class for all web pages,
    all requests and responses from REST API endpoint,
    no direct database manipulation
'''

def index(request):
    '''
        index page/home page
        shows recent available products
    '''

    global cart
    products = requests.get(API_ENDPOINT + '/products')
    products = products.json()

    available_products = []
    for product in products:
        if product["available_quantity"] > 0:
            available_products.append(product)
            if len(available_products) > 15:
                break

    return render(request, 'webs/index.html', {'products': available_products, 'cart': cart})

def about(request):
    '''
        about page for the website
    '''

    return render(request, 'webs/about.html')

def contact(request):
    '''
        contact page for the website
    '''

    return render(request, 'webs/contact.html')

def add_to_cart(request, product_id):
    '''
        adds product to cart
    '''

    global cart
    if product_id not in cart:
        cart.append(int(product_id))

    messages.add_message(request, messages.INFO, 'One Product is added to the cart!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove_from_cart(request, product_id):
    '''
        remove product from cart
    '''

    global cart
    if int(product_id) in cart:
        cart.remove(int(product_id))

    messages.add_message(request, messages.INFO, 'One Product is removed from the cart!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def clear_cart(request):
    '''
        clear all products from cart
    '''

    global cart
    cart = []

    messages.add_message(request, messages.INFO, 'Cart Cleared!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@buyers_only
def checkout(request):
    '''
        checkout page
        shows cart with product details
        summary of all purchase
        remove from cart option
        prepare for placing order by calulating price
    '''

    global cart
    buyer = request.user.id
    products = []
    total = 0

    for product_id in cart:
        product =  requests.get(API_ENDPOINT + '/products/' + str(product_id))
        product = product.json()
        owner = requests.get(product["owner"])
        owner = owner.json()
        total += product["price"]

        product["owner_name"] = owner["username"]
        products.append(product)

    return render(request, 'webs/checkout.html', {'products': products, 'buyer': buyer, 'total': total})

def place_order(request, key, total, buyer, seller, products, quantities):
    '''
        place order action request to the REST API
    '''

    payload = {
        'order_key': key,
        'total': total,
        'status': 'Pending',
        'buyer': buyer,
        'seller': seller,
        'products': products,
        'quantity_list': str(quantities)
    }

    response = requests.post(API_ENDPOINT + '/orders/?post', data=payload)

    if response.status_code >= 300:
        messages.add_message(request, messages.ERROR, 'Error placing new order!')
    else:
        messages.add_message(request, messages.INFO, 'Successfully placed order!')

    response = response.json()
    return response

def update_product(request, product_id, new_available_quantity):
    '''
        update product with new available quantity after selling certain quantity
    '''

    if new_available_quantity < 0:
        new_available_quantity = 0

    payload = {
        'available_quantity': int(new_available_quantity)
    }

    response = requests.put(API_ENDPOINT + '/products/' + product_id + '/', data=payload)
    if response.status_code >= 300:
        messages.add_message(request, messages.ERROR, 'Error updating product!')
    else:
        messages.add_message(request, messages.INFO, 'Successfully updated product!')

@buyers_only
def checkout_request(request):
    '''
        hadles checkout request
        create new orders according to the sellers
        each seller has new orders
        updates product info checkout complete
        clear cart after checkout complete
        shows summary 
    '''

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
    quantity_list = {}
    product_names = {}
    for product_id, quant in zip(product_ids, quantity):
        product = requests.get(API_ENDPOINT + '/products/' + str(product_id))
        product = product.json()

        if product["owner"] not in orders:
            orders[product["owner"]] = []
            total_prices[product["owner"]] = 0
            quantity_list[product["owner"]] = []
            product_names[product["owner"]] = []

        orders[product["owner"]].append(product["url"])
        total_prices[product["owner"]] += (int(quant) * float(product["price"]))
        quantity_list[product["owner"]].append(quant.strip("'"))
        product_names[product["owner"]].append(product["name"])
        new_available_quantity = int(product["available_quantity"]) - int(quant)
        update_product(request, product_id, new_available_quantity)

    placed_orders = []
    for seller, owner_name in zip(orders, owner_names):
        placed_order = place_order(request, order_key, total_prices[seller], buyer, seller, orders[seller], quantity_list[seller])
        placed_order["seller_name"] = owner_name
        placed_order["product_names"] = product_names[seller]
        placed_order["quantity_list"] = quantity_list[seller]
        placed_orders.append(placed_order)

    cart = []
    return render(request, 'webs/complete.html', {'orders': placed_orders})
