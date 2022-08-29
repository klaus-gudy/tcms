from django.db import models

# Create your models here.
class Customer(models.Model):
    account_number = models.IntegerField(unique=True, primary_key=True)
    account_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


    def __str__(self):
        return self.account_name