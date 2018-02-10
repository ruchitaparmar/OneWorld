from django import forms
from .models import Benefactor
# from django.contrib.auth.models import User


class Register(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Benefactor
        fields = ('user', 'password')


class ProfileInfo(forms.ModelForm):
    class Meta:
        model = Benefactor
        exclude = ['user', 'name', 'address']
