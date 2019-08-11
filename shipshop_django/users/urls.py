from django.urls import path, include
from . import views
from users.api import viewsets

'''
    urls for user pages
'''

urlpatterns = [
    path('buyer_profile', views.buyer_profile, name="buyer_profile"),
    path('seller_profile', views.seller_profile, name="seller_profile"),
    path('buyers', viewsets.BuyerListView.as_view()),
    path('sellers', viewsets.SellerListView.as_view()),
    path('buyers/rest_auth/', include('rest_auth.urls')),
    path('sellers/rest_auth/', include('rest_auth.urls')),
    path('buyers/rest_auth/registration/', include('rest_auth.registration.urls')),
    path('sellers/rest_auth/registration/', include('rest_auth.registration.urls')),
]
