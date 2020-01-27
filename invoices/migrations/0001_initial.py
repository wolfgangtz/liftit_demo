# Generated by Django 3.0.2 on 2020-01-27 22:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=100)),
                ('callback_url', models.CharField(max_length=200)),
                ('total_items_price', models.DecimalField(decimal_places=5, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('invoice_number', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=30)),
                ('client_lastname', models.CharField(max_length=30)),
                ('client_id', models.CharField(max_length=30)),
                ('item_code', models.CharField(max_length=30)),
                ('item_description', models.CharField(max_length=100)),
                ('item_amount', models.DecimalField(decimal_places=5, max_digits=20)),
                ('item_price', models.DecimalField(decimal_places=5, max_digits=20)),
                ('item_discount_rate', models.DecimalField(decimal_places=5, max_digits=20)),
            ],
        ),
    ]