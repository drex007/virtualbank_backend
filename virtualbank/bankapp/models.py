from email.policy import default
from django.db import models 
from django.contrib.auth.models import User


class Dashboard(models.Model):
    DIAMOND_BANK = 'DIAMOND BANK'
    UBA_BANK = 'UBA BANK'
    ACCESS_BANK = 'ACCESS BANK'
    ZENITH_BANK = 'ZENITH BANK'
    FIRST_BANK = 'FIRST BANK'
    SELECT_BANK = [

     (DIAMOND_BANK ,'DIAMOND BANK'),
     (UBA_BANK , 'UBA BANK'),
     (ACCESS_BANK , 'ACCESS BANK'),
     (ZENITH_BANK , 'ZENITH BANK' ),
     (FIRST_BANK , 'FIRST BANK')
    ]
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    amount  = models.IntegerField()
    account  = models.IntegerField()
    phone_number = models.CharField(max_length=50)
    bank = models.CharField(max_length=50, choices=SELECT_BANK)
    email = models.EmailField()
    date_opened = models.DateTimeField(auto_now_add=True)
    records = models.ForeignKey('Transactions', on_delete=models.CASCADE, null=True, blank=True)

    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}  {self.last_name} Account "

    

class Transactions(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, blank = True)
    trans_title= models.CharField(max_length=500, null=True, blank=True)
    sender_detail = models.CharField(max_length=500, null=True, blank=True)
    receiver_detail = models.CharField(max_length=500, null=True, blank=True)
    amount_transacted  = models.IntegerField(default=0,)
    account_number = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    bank_of_receiver = models.CharField(max_length=500, blank=True)
    date_of_trans = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.trans_title} | {self.date_of_trans}"

    # def __init__(self, sender_detail, receiver_detail ,amount_to_send:float, account_number,bank_of_receiver):
    #     self.sender_detail = sender_detail 
    #     self.receiver_detail = receiver_detail 
    #     selfrec.amount_to_send = amount_to_send
    #     self.account_number = account_number 
    #     self.bank_of_receiver = bank_of_receiver

    
    def withdrawal(self,receivers_account_number):
        if self.amount > 0 and self.amount_to_send > self.amount:
            amount_left = self.amount - self.amount_to_send
            received = receivers_account_number + self.amount_to_send
            return amount_left
        else:
            print("Please Fund Your Account")
        

    

