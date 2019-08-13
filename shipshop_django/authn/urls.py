from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^user_login', views.LoginView.as_view(), name="login"),
    url(r'^user_logout', views.logout_user, name="logout"),
    url(r'register/', views.RegisterView.as_view(), name="register"),

    # url(r'^login/buyer', views.BuyerLoginView.as_view(), name="buyer_login"),
    # url(r'^login/seller', views.SellerLoginView.as_view(), name="seller_login"),
    # url(r'^logout_buyer', views.logout_buyer, name="logout_buyer"),
    # url(r'^logout_seller', views.logout_seller, name="logout_seller"),
    # url(r'^logout', auth_views.LogoutView.as_view(), name="logout"),
    # url(r'^password_change/done/', auth.views.PasswordChangeDoneView.as_view(template_name='authn/password_change_done.html'), name="password_change_done"),
    # url(r'^password_change/', auth.views.PasswordChangeView.as_view(template_name='authn/password_change_form.html'), name="password_change"),
    # url(r'^password_reset/', auth. views.PasswordResetView.as_view(template_name='authn/password_reset_form.html'), name="password_reset"),
    # url(r'^password_reset/done/', auth.views.PasswordResetDoneView.as_view(template_name='authn/password_reset_done.html'), name="password_reset_done"),
    # path('reset/<uidb64>/<token>', auth.views.PasswordResetConfirmView.as_view(template_name='authn/password_reset_confirm.html'), name="password_reset_confirm"),
    # url(r'reset/done/', auth.views.PasswordResetCompleteView.as_view(template_name='authn/password_reset_complete.html'), name="password_reset_complete"),
    # url(r'register/buyer', views.BuyerRegisterView.as_view(), name="buyer_register"),
    # url(r'register/seller', views.SellerRegisterView.as_view(), name="seller_register")

]
