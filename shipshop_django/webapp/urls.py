from django.urls import path, include
from . import views

'''
    urls for generic web pages
'''

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]
