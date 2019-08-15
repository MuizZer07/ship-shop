from functools import wraps
from django.http import HttpResponseRedirect
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages

'''
    custom decorator class
    restrict access for particular users
'''

def buyers_only(function):
    '''
        only allows for a user who is a buyer, sellers are not allowed
    '''

    @wraps(function)
    def wrap(request, *args, **kwargs):
        usertype = str(request.user)
        if usertype != 'AnonymousUser':
            if request.user.is_buyer:
                 return function(request, *args, **kwargs)
            else:
                messages.add_message(request, messages.INFO, 'You should be logged in as a Buyer!')
                return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.INFO, 'You should be logged in as a Buyer!')
            return HttpResponseRedirect('/user_login/?next=checkout')

    return wrap

def sellers_only(function):
    '''
        only allows for a user who is a seller, sellers are not allowed
    '''

    @wraps(function)
    def wrap(request, *args, **kwargs):
        usertype = str(request.user)
        if usertype != 'AnonymousUser':
            if request.user.is_seller:
                 return function(request, *args, **kwargs)
            else:
                messages.add_message(request, messages.INFO, 'You should be logged in as a Seler!')
                return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.INFO, 'You should be logged in as a Seler!')
            return HttpResponseRedirect('/user_login/?next=checkout')

    return wrap
