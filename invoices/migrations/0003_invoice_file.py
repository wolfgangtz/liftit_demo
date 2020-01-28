# Generated by Django 2.2 on 2020-01-28 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20200128_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='file',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='file', to='invoices.File'),
            preserve_default=False,
        ),
    ]
