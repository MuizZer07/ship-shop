from functools import wraps
from django.http import HttpResponseRedirect
from django.contrib.auth.models import AnonymousUser

def buyers_only(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
    usertype = str(request.user)
    if usertype != 'AnonymousUser':
        if request.user.is_buyer:
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

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
