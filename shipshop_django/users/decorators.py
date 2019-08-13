from functools import wraps
from django.http import HttpResponseRedirect
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages

def buyers_only(function):
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
  @wraps(function)
  def wrap(request, *args, **kwargs):
    usertype = str(request.user)
    if usertype != 'AnonymousUser':
        if request.user.is_seller:
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

  return wrap
