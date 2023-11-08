from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import *
import json


class DateInput(forms.DateInput):
    input_type = 'date'


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(
                            widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
                            required=True)
    password = forms.CharField(
                            widget=forms.PasswordInput(attrs={'id': 'floatingPassword', 'class': 'form-control mb-3'}),
                            required=True)


    class Meta:
        model=User
        fields=['username','password']



class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'client_logo', 'address_line_1', 'province', 'postal_code', 'phone_number', 'email_address', 'tax_number']



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'quantity', 'price', 'currency']


class InvoiceForm(forms.ModelForm):
    due_date = forms.DateField(
                        required = True,
                        label='Invoice Due',
                        widget=DateInput(attrs={'class': 'form-control'}),)

    class Meta:
        model = Invoice
        fields = ['title', 'number', 'due_date', 'payment_terms', 'status', 'notes', 'client', 'product']


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['client_name', 'client_logo', 'address_line_1', 'province', 'postal_code', 'phone_number', 'email_address', 'tax_number']




# <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
# <input type="password" class="form-control" id="floatingPassword" placeholder="Password">