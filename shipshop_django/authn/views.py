from django.shortcuts import render, redirect
from django.views.generic import FormView
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from shipshop_django import settings
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.template.loader import get_template
from django.contrib import messages
from django.urls import reverse
import requests

def register_buyer(request):
    return render(request, 'registration/register_buyer.html')

def register_new_buyer(form, request):
    payload = {
        'email': form.cleaned_data.get('email'),
        'username': form.cleaned_data.get('username'),
        'first_name': form.cleaned_data.get('first_name'),
        'last_name': form.cleaned_data.get('last_name'),
        'password1': form.cleaned_data.get('password'),
        'password2': form.cleaned_data.get('confirm_password'),
    }
    response = requests.post(settings.API_ENDPOINT + '/buyers/rest_auth/registration/', data=payload)

    if response.status_code >= 300:
        messages.add_message(request, messages.ERROR, 'Registration Error!')
        response = response.json()
    else:
        messages.add_message(request, messages.INFO, 'Successfully Registered!')
        response = response.json()
        request.session['key'] = response['key']
    return response

class BuyerRegisterForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_password_confirm(self):
        cleaned_data = super().clean()

        if form.cleaned_data.get('password') != form.cleaned_data.get('confirm_password'):
            raise ValidationError('Password fields do not match')

class BuyerRegisterView(FormView):
    template_name = "registration/register_buyer.html"
    form_class = BuyerRegisterForm
    success_url = '/'

    def form_valid(self, form):
        try:
            response = register_new_buyer(form, self.request)
            messages.add_message(self.request, messages.INFO, response)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        except IntegrityError as e:
            return redirect('/buyer_register')

def login_buyer(request):
    return render(request, 'authn/buyer_login.html')

def login_a_buyer(request, username, password):
    payload = {
        'username': username,
        'password': password
    }

    response = requests.post(settings.API_ENDPOINT + '/buyers/rest_auth/login/', data=payload)

    if response.status_code >= 300:
        messages.add_message(request, messages.ERROR, 'Sign in Error!')
    else:
        messages.add_message(request, messages.INFO, 'Successfully Signed In!')
        response = response.json()
        request.session['key'] = response['key']
    return response

def logout_buyer(request):
    if 'key' in request.session['key']:
        payload = {
            'key': request.session['key'],
        }
        response = requests.post(settings.API_ENDPOINT + '/buyers/rest_auth/logout/', data=payload)
        print(response.status_code)
        if response.status_code >= 300:
            messages.add_message(request, messages.ERROR, 'Sign out Error!')
        else:
            messages.add_message(request, messages.INFO, 'Successfully Signed Out!')
            request.session.pop('key', request.session['key'])
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
    else:
        messages.add_message(request, messages.INFO, 'You are not Signed In!')
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)

class BuyerLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class BuyerLoginView(FormView):
    template_name = "authn/login_buyer.html"
    form_class = BuyerLoginForm
    success_url = '/'

    def form_valid(self, form):
        try:
            response = login_a_buyer(self.request, form.cleaned_data['username'], form.cleaned_data['password'])
            print(response)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        except IntegrityError as e:
            return redirect('/')

def register_seller(request):
    return render(request, 'registration/register_seller.html')

def register_new_seller(form, request):
    payload = {
        'email': form.cleaned_data.get('email'),
        'username': form.cleaned_data.get('username'),
        'first_name': form.cleaned_data.get('first_name'),
        'last_name': form.cleaned_data.get('last_name'),
        'password1': form.cleaned_data.get('password'),
        'password2': form.cleaned_data.get('confirm_password'),
    }
    response = requests.post(settings.API_ENDPOINT + '/sellers/rest_auth/registration/', data=payload)

    if response.status_code >= 300:
        messages.add_message(request, messages.ERROR, 'Registration Error!')
        response = response.json()
    else:
        messages.add_message(request, messages.INFO, 'Successfully Registered!')
        response = response.json()
        request.session['key'] = response['key']
    return response

class SellerRegisterForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_password_confirm(self):
        cleaned_data = super().clean()

        if form.cleaned_data.get('password') != form.cleaned_data.get('confirm_password'):
            raise ValidationError('Password fields do not match')

class SellerRegisterView(FormView):
    template_name = "registration/register_seller.html"
    form_class = SellerRegisterForm
    success_url = '/'

    def form_valid(self, form):
        try:
            response = register_new_seller(form, self.request)
            messages.add_message(self.request, messages.INFO, response)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        except IntegrityError as e:
            return redirect('/seller_register')

def login_seller(request):
    return render(request, 'authn/seller_login.html')

def login_a_seller(request, username, password):
    payload = {
        'username': username,
        'password': password
    }

    response = requests.post(settings.API_ENDPOINT + '/sellers/rest_auth/login/', data=payload)

    if response.status_code >= 300:
        messages.add_message(request, messages.ERROR, 'Sign in Error!')
    else:
        messages.add_message(request, messages.INFO, 'Successfully Signed In!')
        response = response.json()
        request.session['key'] = response['key']
    return response

def logout_seller(request):
    if 'key' in request.session['key']:
        payload = {
            'key': request.session['key'],
        }
        response = requests.post(settings.API_ENDPOINT + '/sellers/rest_auth/logout/', data=payload)

        if response.status_code >= 300:
            messages.add_message(request, messages.ERROR, 'Sign out Error!')
        else:
            messages.add_message(request, messages.INFO, 'Successfully Signed Out!')

        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
    else:
        messages.add_message(request, messages.INFO, 'You are not Signed In!')
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)

class SellerLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SellerLoginView(FormView):
    template_name = "authn/login_seller.html"
    form_class = SellerLoginForm
    success_url = '/'

    def form_valid(self, form):
        try:
            response = login_a_seller(self.request, form.cleaned_data['username'], form.cleaned_data['password'])
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        except IntegrityError as e:
            return redirect('/')
