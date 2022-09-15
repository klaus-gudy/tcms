from django.db import models

import datetime

from django.contrib.auth import get_user_model

User = get_user_model()

class Customer(models.Model):
    ACCOUNTS = [
        ('M', 'Malkia'),('R', 'Salary'),
        ('S', 'Savings'),('T', 'Tanzanite'),
        ('J', 'Junior'),('A', 'Scholar'),
        ('F', 'Fixed'),('D', 'Dhahabu'),
    ]

    account_number = models.IntegerField(unique=True, primary_key=True)
    account_name = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    age = models.PositiveIntegerField(null=True, blank=True)
    acc_type = models.CharField(max_length=100, choices=ACCOUNTS,null=True, blank=True)

    # class Meta:
    #     ordering = ['account_name']
    #     verbose_name = 'Customer'
    #     verbose_name_plural = 'Customers'

    def __str__(self):
        return self.account_name.username