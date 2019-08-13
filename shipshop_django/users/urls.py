from django.urls import path, include
from . import views

'''
    urls for user pages
'''

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('api/rest_auth/', include('rest_auth.urls')),
    path('api/rest_auth/registration', include('rest_auth.registration.urls')),
]
