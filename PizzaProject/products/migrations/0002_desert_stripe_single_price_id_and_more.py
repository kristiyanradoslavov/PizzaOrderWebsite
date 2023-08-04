# Generated by Django 4.2.3 on 2023-08-02 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='desert',
            name='stripe_single_price_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drink',
            name='stripe_large_price_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drink',
            name='stripe_small_price_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='salad',
            name='stripe_large_price_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='salad',
            name='stripe_small_price_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='drink',
            name='small_image',
            field=models.ImageField(upload_to='images/products/drink'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='stripe_extra_large_price_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='stripe_large_price_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='stripe_medium_price_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='stripe_small_price_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]