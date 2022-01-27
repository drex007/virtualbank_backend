"""virtualbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bankapp.views import user_dashboard,logoutPage,home,check_transactions, make_transactions,loggin, deposit, get_balance, signup


urlpatterns = [
    path('admin/', admin.site.urls),
     path('',loggin , name='loggin'),
    path('dashboard/<int:pk>/', user_dashboard, name='user-dashboard'),
     path('make_transactions/',make_transactions, name='transactions'),
      path('getbalance/<int:pk>',get_balance, name='balance'),
      path('singup/',signup, name='signup'),
       path('loggedout/',logoutPage, name='logout'),
    path('transactions/',check_transactions, name='check-transactions'),
    path('deposits/',deposit, name='deposit'),
    
    path('home/',home, name='home'),
    

  
]