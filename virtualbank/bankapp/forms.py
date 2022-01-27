from email.policy import default
from random import choices
from unittest.mock import DEFAULT
from django.forms import ModelForm
from django import forms
from .models import Dashboard,Transactions
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, label= 'password')


class DashForm(ModelForm):
    class Meta:
        model = Dashboard
        fields = '__all__'
        exclude = ['date_opened','records','date_updated']


class DepositForm(forms.Form):
    deposit = forms.IntegerField(label='deposit', min_value =0)
    # password = forms.CharField(widget=forms.PasswordInput, label= 'password')


class TransactionForm(forms.Form):
    account_number = forms.CharField(label='Account Number', max_length=50)
    description = forms.CharField(label='Description', max_length=50)
    amount = forms.IntegerField(label='Amount', min_value=0)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields =  ["username", "email", "password1", "password2" ]
class SignUpForm2(forms.Form):
    DEFAULTBANK = 'XXXXXXXXX'
    DIAMOND_BANK = 'DIAMOND BANK'
    UBA_BANK = 'UBA BANK'
    ACCESS_BANK = 'ACCESS BANK'
    ZENITH_BANK = 'ZENITH BANK'
    FIRST_BANK = 'FIRST BANK'

    SELECT_BANK = [
     (DEFAULTBANK ,'XXXXXXXXX'),
     (DIAMOND_BANK ,'DIAMOND BANK'),
     (UBA_BANK , 'UBA BANK'),
     (ACCESS_BANK , 'ACCESS BANK'),
     (ZENITH_BANK , 'ZENITH BANK' ),
     (FIRST_BANK , 'FIRST BANK')
    ]
    firstname = forms.CharField(label='firstname', max_length=50)
    lastname = forms.CharField(label='lastname', max_length=50)
    phonenumber = forms.IntegerField(label='phonenumber', min_value=0)
    bank = forms.ChoiceField(label='bank',  choices= SELECT_BANK)






# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username','email', ] 



# class TransactionForm(ModelForm):
#     class Meta:
#         model = Transactions
#         fields = '__all__'
#         exclude = ['date_of_trans','trans_title']