from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

'''
    urls for authentication pages
'''

urlpatterns = [
    url(r'^user_login', views.LoginView.as_view(), name="login"),
    url(r'^user_logout', views.logout_user, name="logout"),
    url(r'register/', views.RegisterView.as_view(), name="register"),
    url(r'forgot_password_page/', views.forgot_password_page, name="forgot_password_page"),
    url(r'forgot_password_request/', views.forgot_password_request, name="forgot_password_request"),
    url(r'password_reset_confirm/<uidb64>/<token>', views.password_reset_confirm, name="password_reset_confirm"),
    url(r'change_password_page/', views.change_password_page, name="change_password_page"),
    url(r'change_password_request/', views.change_password_request, name="change_password_request")
]
