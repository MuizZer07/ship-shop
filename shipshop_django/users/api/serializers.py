from rest_framework import serializers
from users.models import User
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.utils.translation import gettext as _
from django.db import IntegrityError

'''
    serializers for User model
    registraion serializer
'''

class UserSerializer(serializers.HyperlinkedModelSerializer):
    '''
        User serializer for API endpoint
    '''

    class Meta:
        model = User
        fields = ('id', 'url', 'first_name', 'last_name', 'username', 'email', 'is_buyer', 'is_seller', 'phone_number', 'rating')

class RegisterSerializer(serializers.Serializer):
    '''
        custom registraion serializer
        including custom parameters and validations
    '''

    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    username = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    buyer = serializers.BooleanField(required=True, write_only=True)
    seller = serializers.BooleanField(required=True, write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_username(self, username):
        username = get_adapter().clean_email(username)
        users = User.objects.filter(username=username)

        if len(users) > 0:
            raise serializers.ValidationError(
                _("Username is already taken."))

        return username

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                _("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'is_buyer': self.validated_data.get('buyer', ''),
            'is_seller': self.validated_data.get('seller', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.is_buyer = self.cleaned_data['is_buyer']
        user.is_seller = self.cleaned_data['is_seller']
        user.save()
        return user
