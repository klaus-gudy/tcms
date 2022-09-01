from django.contrib import admin

from .models import Deposit

# Register your models here.
class DepositAdmin(admin.ModelAdmin):
    list_display = ['amount', 'my_account', 'complete', 'date']

admin.site.register(Deposit, DepositAdmin)