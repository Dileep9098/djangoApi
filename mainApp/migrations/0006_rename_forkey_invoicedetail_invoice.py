# Generated by Django 4.2.4 on 2024-01-01 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_rename_invoice_invoicedetail_forkey'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoicedetail',
            old_name='forkey',
            new_name='invoice',
        ),
    ]
