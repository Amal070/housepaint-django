# Generated by Django 4.1.2 on 2024-01-11 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paint_app', '0009_remove_message_client_message_client_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_id', models.IntegerField(blank=True, null=True)),
                ('client_id', models.IntegerField(blank=True, null=True)),
                ('bill_no', models.IntegerField(blank=True, null=True)),
                ('package_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Package Name')),
                ('package_price', models.IntegerField(blank=True, null=True)),
                ('shop_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Shop Name')),
                ('shop_phone', models.IntegerField(blank=True, null=True)),
                ('client_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Client Name')),
                ('client_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Client Address')),
                ('square_feet', models.CharField(blank=True, max_length=100, null=True, verbose_name='Square Feet')),
                ('square_feet_rate', models.IntegerField(blank=True, null=True)),
                ('product_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Site Name')),
                ('total_price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
