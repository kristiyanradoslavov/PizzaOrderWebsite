# Generated by Django 4.2.3 on 2023-07-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_orderitem_id_alter_orderitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price_id',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]