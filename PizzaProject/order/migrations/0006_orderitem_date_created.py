# Generated by Django 4.2.3 on 2023-08-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_orderhistory_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
