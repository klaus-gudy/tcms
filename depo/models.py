from django.db import models
from cust.models import Customer
from django.contrib.auth.models import User

import uuid

# Create your models here.
class Deposit(models.Model):
    amount=models.FloatField()
    my_account = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    # account=models.CharField(max_length=100)
    date =models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    token =  models.UUIDField(editable=False, unique=True,primary_key=False,default=uuid.uuid4())

    def __str__(self):
        return str(self.id)

