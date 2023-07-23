# Generated by Django 4.2.3 on 2023-07-19 08:54

import PizzaProject.products.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[PizzaProject.products.validators.name_validator, django.core.validators.MinLengthValidator(2)])),
                ('description', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5)])),
                ('price_small', models.FloatField(validators=[PizzaProject.products.validators.positive_price])),
                ('price_medium', models.FloatField(validators=[PizzaProject.products.validators.positive_price])),
                ('price_large', models.FloatField(validators=[PizzaProject.products.validators.positive_price])),
                ('price_extra_large', models.FloatField(validators=[PizzaProject.products.validators.positive_price])),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/products/pizza')),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
        ),
    ]
