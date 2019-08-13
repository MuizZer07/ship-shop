from django.urls import path, include
from . import views
from django.conf.urls import url

'''
    urls for CRUD operations
'''

urlpatterns = [
    url(r'^show/(\d+)', views.show_product , name="show_product"),
    url(r'^edit/(\d+)', views.edit_product , name="edit_product"),
    url(r'^show_list/', views.show_list , name="show_list"),
    url(r'^edit_product_request/(\d+)', views.edit_product_request , name="edit_product_request"),
    url(r'^add/', views.add_product , name="add_product"),
    url(r'^add_product_request/', views.add_product_request , name="add_product_request"),
    url(r'^delete/(\d+)', views.delete_product , name="delete_product"),
]
