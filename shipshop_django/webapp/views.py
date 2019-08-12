from django.shortcuts import render
import requests
from shipshop_django.settings import API_ENDPOINT

'''
    Frontend,
    view class for all web pages,
    all requests and responses from REST API endpoint,
    no direct database manipulation
'''

def index(request):
    products = requests.get(API_ENDPOINT + '/products')
    products = products.json()

    print(request.user)
    if 'key'in request.session:
        print(request.session['key'])

    return render(request, 'webs/index.html', {'products': products})

def about(request):
    return render(request, 'webs/about.html')

def contact(request):
    return render(request, 'webs/contact.html')
