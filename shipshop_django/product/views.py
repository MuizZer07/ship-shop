from django.shortcuts import render, redirect
import requests
from shipshop_django.settings import API_ENDPOINT
from django.contrib import messages

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

    return render(request, 'product/show.html', {'product': product})

def add_product(request):
    '''
        add new product form

        return: form to add product
    '''

    return render(request, 'product/create.html')

def add_product_request(request):
    '''
        handles add product form
        post it to database through REST API Call

        return: index with message (error/success)
    '''

    payload = request.POST
    images = {'image': request.FILES['image']}

    response = requests.post(API_ENDPOINT + '/products/?post', data=payload,files=images)

    if response.status_code >= 300:
        messages.add_message(request, messages.ERROR, 'Error adding new product!')
    else:
        messages.add_message(request, messages.INFO, 'Successfully added new product!')

    response = response.json()
    return redirect('index')

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
    return redirect('index')

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

    return render(request, 'product/edit.html', {'product': product})

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

    if len(request.FILES):
        images = {'image': request.FILES['image']}
        response = requests.put(API_ENDPOINT + '/products/' + product_id + '/', data=payload, files=images)
    else:
        response = requests.put(API_ENDPOINT + '/products/' + product_id + '/', data=payload)

    if response.status_code >= 300:
        messages.add_message(request, messages.ERROR, 'Error adding new product!')
    else:
        messages.add_message(request, messages.INFO, 'Successfully added new product!')

    return redirect('index')
