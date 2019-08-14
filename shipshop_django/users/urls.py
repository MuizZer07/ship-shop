from django.urls import path, include
from . import views
from django.conf.urls import url

'''
    urls for user pages
'''

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    url('profile/(\d+)', views.profile, name="profile"),
    path('api/rest_auth/', include('rest_auth.urls')),
    path('api/rest_auth/registration', include('rest_auth.registration.urls')),
]
