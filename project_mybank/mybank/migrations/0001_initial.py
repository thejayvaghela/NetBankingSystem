# Generated by Django 3.1.2 on 2020-11-05 06:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('current_balance', models.FloatField(validators=[django.core.validators.MinValueValidator(3000.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(validators=[django.core.validators.MaxValueValidator(100000.0)])),
            ],
        ),
    ]
