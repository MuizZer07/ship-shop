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
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

'''
    - user registration
    - classes and helper functions
'''
def register(request):
    '''
        render registraion form
    '''

    return render(request, 'registration/register_user.html')

def register_new_user(form, request):
    '''
        registraion request to REST API endpoint

        return response from API
    '''
    payload = {
        'email': form.cleaned_data.get('email'),
        'username': form.cleaned_data.get('username'),
        'first_name': form.cleaned_data.get('first_name'),
        'last_name': form.cleaned_data.get('last_name'),
        'password1': form.cleaned_data.get('password'),
        'password2': form.cleaned_data.get('confirm_password'),
        form.cleaned_data.get('register_as'): True
    }
    response = requests.post(settings.API_ENDPOINT + '/rest_auth/registration', data=payload)

    if response.status_code >= 300:
        messages.add_message(request, messages.ERROR, 'Registration Error!')
        response = response.json()

        for resp in response:
            for res in response[resp]:
                messages.add_message(request, messages.ERROR, res)
        response['data'] = 'error'
    else:
        messages.add_message(request, messages.INFO, 'Successfully Registered!')
        response = response.json()
        request.session['key'] = response['key']
        response['data'] = 'success'
    return response

class RegisterForm(forms.Form):
    '''
        django form template for registration with validation
    '''
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    options =[("buyer", "Buyer"), ("seller", "Seller")]
    register_as = forms.ChoiceField(choices=options, label="Register As")

    def clean_password_confirm(self):
        cleaned_data = super().clean()

        if form.cleaned_data.get('password') != form.cleaned_data.get('confirm_password'):
            raise ValidationError('Password fields do not match')

class RegisterView(FormView):
    '''
        registraion form handling
    '''

    template_name = "registration/register_user.html"
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        try:
            response = register_new_user(form, self.request)

            if response['data'] != 'error':
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
            else:
                return  redirect('/register')
        except IntegrityError as e:
            return redirect('/register')

'''
    - user login
    - classes and helper functions
'''
def login_user(request):
    '''
        generic login page for users
    '''

    return render(request, 'authn/login_user.html')

def login_a_user(request, username, password):
    '''
        login request to REST API endpoint
    '''

    payload = {
        'username': username,
        'password': password
    }

    response = requests.post(settings.API_ENDPOINT + '/rest_auth/login/', data=payload)

    if response.status_code >= 300 and response.status_code < 400:
        messages.add_message(request, messages.ERROR, 'Sign in Error!')
        response = response.json()

        for res in  response['non_field_errors']:
            messages.add_message(request, messages.ERROR, res)

        response['data'] = 'error'
    elif response.status_code >= 400:
        messages.add_message(request, messages.ERROR, 'Sign in Error!')
        response = {}
        response['data'] = 'error'
    else:
        messages.add_message(request, messages.INFO, 'Successfully Signed In!')
        response = response.json()
        if 'key' in response:
            request.session['key'] = response['key']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
        response['data'] = 'success'
    return response

class LoginForm(forms.Form):
    '''
        login form template
    '''

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class LoginView(FormView):
    '''
        login request handling with validation
    '''

    template_name = "authn/login_user.html"
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        try:
            response = login_a_user(self.request, form.cleaned_data['username'], form.cleaned_data['password'])

            if response['data'] != 'error':
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
            else:
                return redirect('/user_login')

        except IntegrityError as e:
            return redirect('/user_login')

'''
    user logout function
'''
def logout_user(request):
    '''
        logout request to REST API
    '''

    payload = {
        'key': request.session['key'],
    }
    response = requests.post(settings.API_ENDPOINT + '/rest_auth/logout/', data=payload)

    if response.status_code >= 300:
        messages.add_message(request, messages.ERROR, 'Sign out Error!')
    else:
        messages.add_message(request, messages.INFO, 'Successfully Signed Out!')
        request.session.pop('key', request.session['key'])
        logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
    return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)

def forgot_password_page(request):
    '''
        forgot password page
    '''

    return render(request, 'authn/password_reset_form.html')

def forgot_password_request(request):
    '''
        forgot passward request

        ### HAS ERRORS TO BE FIXED! ###
    '''

    payload = {
        'email': request.POST.get('email'),
    }
    response = requests.post(settings.API_ENDPOINT + '/rest_auth/password/reset/', data=payload)
    print(response)

    return render(request, 'authn/password_reset_form.html')

def password_reset_confirm(request, uidb64, token):
    '''
        should return confirmation of resetting password

        ### DOESN'T WORK ###
    '''

    return render(request, 'authn/password_reset_confirm.html')

@login_required
def change_password_page(request):
    '''
        change password page
    '''

    return render(request, 'authn/password_change_form.html')

@login_required
def change_password_request(request):
    '''
        send request for changing password to API

        ### SOME AUTHENTICATION ERROR HERE, NEED TO FIX ###
    '''
    
    payload = {
        'old_password': request.POST.get('old_password'),
        'new_password1': request.POST.get('new_password1'),
        'new_password2': request.POST.get('new_password2'),
    }
    headers = {'Content-Type':'application/json',
               'Authorization': 'Token {}'.format(request.session['key'])}

    response = requests.post(settings.API_ENDPOINT + '/rest_auth/password/change/', data=payload, headers=headers).json()

    return render(request, 'authn/password_change_done.html')
