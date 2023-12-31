# Generated by Django 4.2.3 on 2023-08-02 17:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0002_orderitem_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3)])),
                ('product_id', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('size', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('single_price', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('price_id', models.CharField(max_length=40)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
