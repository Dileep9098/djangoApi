# Generated by Django 4.2.4 on 2024-01-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_alter_invoicedetail_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoiceF',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
    ]
