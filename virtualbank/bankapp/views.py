import email
from re import A
from random import randint 
from django.dispatch import receiver
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from .forms import DashForm,TransactionForm, DepositForm,LoginForm, SignUpForm, SignUpForm2
from .models import Dashboard, Transactions
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404


from .models import *


def home(request):
    return render (request, 'index.html', {})

def signup(request):  
    if request.method == 'POST':
        accountnumber = randint(1000000000,2000000000)
        forms = SignUpForm(request.POST)
        second_form = SignUpForm2(request.POST)
        if forms.is_valid() and second_form.is_valid():
            user = forms.save(commit=False)
            user.username = user.username.lower()
            user.save()
            new_user = Dashboard.objects.create(username=user,
            first_name =  second_form.cleaned_data['firstname'], last_name = second_form.cleaned_data['lastname'],
            amount = 0, account = accountnumber, phone_number = second_form.cleaned_data['phonenumber'],
            bank = second_form.cleaned_data['bank'], email =user.email )
            new_user.save()
            
            print("reg successful")
            return redirect('loggin')

    forms  = SignUpForm()
    second_form  = SignUpForm2()
    context = {'forms': forms, 'second_form': second_form}
    return render(request,'signup.html', context)
            
def loggin(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data['username'].lower()
            password = loginform.cleaned_data['password']
            try:
                user = User.objects.get(username = username )
            except:
                 return HttpResponse("User Does Not Exist")

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect ('home')
        else:
            return HttpResponse("Username or password not correct")
    else:
        loginform = LoginForm()

    context = {'loginform': loginform, 'page':page }
    return render (request,'login.html', context)


def send_email(request):
    pass 


#MAke A Transfer
def make_transactions(request):
    title = "Transfer"

    if request.method == 'POST':
        forms = TransactionForm(request.POST)
        if forms.is_valid():
            account = forms.cleaned_data['account_number']
            descriptions= forms.cleaned_data['description']
            amount_to_be_sent = forms.cleaned_data['amount']
            if Dashboard.objects.filter(account= account).exists():
                receivers_detail, created = Dashboard.objects.get_or_create(account=account)
                senders_detail,created2 = Dashboard.objects.get_or_create(username=request.user )
                print(senders_detail.amount)
                print(account, descriptions,amount_to_be_sent)
                if senders_detail.amount > 0 and senders_detail.amount > amount_to_be_sent:
                    transaction = Transactions.objects.create(customer=senders_detail.username
                    ,trans_title = title, 
                    sender_detail= (senders_detail.first_name, senders_detail.last_name),
                    
                    receiver_detail = (receivers_detail.first_name, receivers_detail.last_name),
                    amount_transacted= amount_to_be_sent
                    ,account_number =receivers_detail.account,
                    bank_of_receiver = receivers_detail.bank, 
                    description=title,
                  )
                    receivers_detail.amount = receivers_detail.amount + amount_to_be_sent
                    receivers_detail.save()
                    senders_detail.amount = senders_detail.amount - amount_to_be_sent
                    senders_detail.save()
                    
                    return HttpResponse("Transfer succesful")
                    
                else: 
                    print("Ïnsufficeint Fund")
                    return HttpResponse("Insufficient Fund, Fund account Please ")        
             
            else:
                print("Wrong Account Number please check account details")
                return HttpResponse("Wrong Account Number please check account details")                  
    forms = TransactionForm()
    context = {'forms': forms }
    return render (request,'make_transactions.html' ,context)


#Make deposit 
def deposit(request):
    title = "Deposit"
    # current_user = User.objects.get(username=request.user)
    current_user = get_object_or_404(User, username =request.user)
  

    if request.method == 'POST':
        forms = DepositForm(request.POST)
        if forms.is_valid():
            current_detail, created = Dashboard.objects.get_or_create(username=request.user)
            amount_deposited = forms.cleaned_data['deposit']
            current_detail.amount = current_detail.amount + amount_deposited       
            deposit = Transactions.objects.create(customer = current_user, trans_title =title,
            sender_detail=(current_detail.first_name, current_detail.last_name),
            receiver_detail=(current_detail.first_name, current_detail.last_name) ,amount_transacted=amount_deposited,
            account_number = current_detail.account, description=title,bank_of_receiver= current_detail.bank)
            
            current_detail.save()
            deposit.save()
         
            print('deposit succesful')
            return redirect('home')
    forms = DepositForm()
    context = {'forms': forms}
    
    return render(request, 'deposit.html', context )
        
# Check Transaction History
def check_transactions(request):
    current_user = get_object_or_404(User, username =request.user)
    # current_user = User.objects.get(username=request.user)
    trans = current_user.transactions_set.all()
    context = {'transactions': trans}
    return render (request, 'transactions.html', context)


def send_complain(request):
    pass 




def user_dashboard(request, pk):
    user = get_object_or_404(Dashboard, username =request.user)
    
    bank = user.bank
    firstname = user.first_name
    secondname = user.last_name
    accountnumber = user.account
    phone= user.phone_number
    emailaddress = user.email

    context = {
        'bank': bank,
     'firstname' : firstname,
    'secondname': secondname,
    'accountnumber' : accountnumber,
     'phone': phone,
     'emailaddress' : emailaddress
    }            

    return render(request,'dashboard.html', context)


def get_balance(request):
    user = get_object_or_404(Dashboard, username= request.user)
    # user = Dashboard.objects.get(id=pk)
    balance = user.amount
    username = user.username
    context = {'balance': balance,'user': user}
    print(balance)
    print(username)
    return render(request, 'balance.html', context)

def logoutPage(request):
    logout(request)
    return redirect('loggin')


