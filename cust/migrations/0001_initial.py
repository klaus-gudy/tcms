# Generated by Django 4.0.1 on 2022-08-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('account_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('account_name', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('nida_number', models.IntegerField(unique=True)),
                ('address', models.CharField(max_length=255)),
                ('occupation', models.CharField(default='Not Enter', max_length=100)),
            ],
        ),
    ]