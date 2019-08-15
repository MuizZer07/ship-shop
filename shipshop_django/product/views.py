from django.shortcuts import render, redirect
import requests
from shipshop_django.settings import API_ENDPOINT
from django.contrib import messages
from webapp.global_variables import cart, categories
import re
from users.decorators import sellers_only

'''
    view class to perform CRUD operations
    from templates via REST api calls
'''

def show_product(request, product_id):
    '''
        shows a single product to template
        input: product_id

        return: product details page
    '''

    product = requests.get(API_ENDPOINT + '/products/' + str(product_id))
    product = product.json()

    return render(request, 'product/show.html', {'product': product, 'cart': cart})

@sellers_only
def show_list(request):
    '''
        show list of products for a seller
        input: user id (owner)

        return: list of products
    '''

    products = requests.get(API_ENDPOINT + '/products')
    products = products.json()

    my_products = []
    for product in products:
        if product['owner'].split("/")[-2] == str(request.user.id):
            my_products.append(product)

    return render(request, 'product/show_list.html', {'products': my_products})

def show_list_by_category(request, category):
    '''
        show list of products by a category
        input: category (string)

        return: list of products
    '''

    products = requests.get(API_ENDPOINT + '/products')
    products = products.json()

    my_products = []
    for product in products:
        if re.sub('[^A-Za-z0-9]+', '', product['category']) == category and product['available_quantity'] > 0:
            my_products.append(product)

    count = len(my_products)
    return render(request, 'product/show_list_by_category.html', {'products': my_products, 'cart': cart, 'count': count})

def show_all(request):
    '''
        show list of all available products

        return: list of products
    '''

    global cart
    products = requests.get(API_ENDPOINT + '/products')
    products = products.json()

    available_products = []
    for product in products:
        if product["available_quantity"] > 0:
            available_products.append(product)

    return render(request, 'product/all_products.html', {'products': available_products, 'cart': cart})

@sellers_only
def add_product(request):
    '''
        add new product form

        return: form to add product
    '''

    return render(request, 'product/create.html', {'categories': categories})

@sellers_only
def add_product_request(request):
    '''
        handles add product form
        post it to database through REST API Call

        return: index with message (error/success)
    '''

    images = {'image': request.FILES['image']}
    user = requests.get(API_ENDPOINT + '/users/' + str(request.user.id)).json()

    payload = {
        'name': request.POST.get('name'),
        'description': request.POST.get('description'),
        'available_quantity': request.POST.get('available_quantity'),
        'price': request.POST.get('price'),
        'category': request.POST.get('category_id'),
        'owner': user["url"]
    }

    response = requests.post(API_ENDPOINT + '/products/?post', data=payload,files=images)
    if response.status_code >= 300:
        messages.add_message(request, messages.ERROR, 'Error adding new product!')
    else:
        messages.add_message(request, messages.INFO, 'Successfully added new product!')

    response = response.json()
    print(response)
    return redirect('index')

@sellers_only
def delete_product(request, product_id):
    '''
        deletes a product from the database
        through REST API call

        input: product_id
        return: index with message (error/success)
    '''

    response = requests.delete(API_ENDPOINT + '/products/' + product_id + '/?delete')

    if response.status_code >= 300:
        messages.add_message(request, messages.ERROR, 'Error deleting new product!')
    else:
        messages.add_message(request, messages.INFO, 'Successfully deleted!')
    return redirect('show_list')

@sellers_only
def edit_product(request, product_id):
    '''
        update info of a product
        shows a form with previous value
        through REST API call

        input: product_id
        return: form with previous value
    '''

    product = requests.get(API_ENDPOINT + '/products/' + str(product_id))
    product = product.json()

    return render(request, 'product/edit.html', {'product': product, 'categories': categories})

@sellers_only
def edit_product_request(request, product_id):
    '''
        handles form to update a product
        through REST API call

        return: index with message (error/success)
    '''

    payload = {}
    for info in request.POST:
        if request.POST[info] != '':
            payload[info] = request.POST[info]

    if len(request.FILES) > 0:
        images = {'image': request.FILES['image']}
        response = requests.put(API_ENDPOINT + '/products/' + product_id + '/', data=payload, files=images)
    else:
        response = requests.put(API_ENDPOINT + '/products/' + product_id + '/', data=payload)

    if response.status_code >= 300:
        messages.add_message(request, messages.ERROR, 'Error adding new product!')
    else:
        messages.add_message(request, messages.INFO, 'Successfully added new product!')

    return redirect('show_list')
