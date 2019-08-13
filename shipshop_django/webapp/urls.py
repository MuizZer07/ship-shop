from django.urls import path, include
from . import views
from django.conf.urls import url

'''
    urls for generic web pages
'''

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('checkout/', views.checkout, name="checkout"),
    path('checkout_request/', views.checkout_request, name="checkout_request"),
    url(r'^add_to_cart/(\d+)', views.add_to_cart , name="add_to_cart"),
    url(r'^remove_from_cart/(\d+)', views.remove_from_cart , name="remove_from_cart"),
]
