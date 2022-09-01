from django.contrib import admin
from .models import *

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['account_number', 'account_name', 'address', 'age', 'acc_type']

admin.site.register(Customer, CustomerAdmin)