from django.urls import path, include
from . import views
from django.conf.urls import url

'''
    urls for CRUD operations
'''

urlpatterns = [
    url(r'^login', views.login , name="login"),
]
