# Generated by Django 4.0.1 on 2022-08-29 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cust', '0002_remove_customer_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='nida_number',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='occupation',
        ),
    ]