from django.db import models

import datetime

# Create your models here.
class Customer(models.Model):
    ACCOUNTS = [
        ('M', 'Malkia'),('R', 'Salary'),
        ('S', 'Savings'),('T', 'Tanzanite'),
        ('J', 'Junior'),('A', 'Scholar'),
        ('F', 'Fixed'),('D', 'Dhahabu'),
    ]

    account_number = models.IntegerField(unique=True, primary_key=True)
    account_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.PositiveIntegerField(null=True, blank=True)
    acc_type = models.CharField(max_length=100, choices=ACCOUNTS,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['account_name']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.account_name