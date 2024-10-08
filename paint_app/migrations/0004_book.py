# Generated by Django 4.1.2 on 2024-01-10 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paint_app', '0003_package'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_id', models.IntegerField(blank=True, null=True)),
                ('shop_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Shop Name')),
                ('shop_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Shop address')),
                ('shop_phone', models.IntegerField(blank=True, max_length=100, null=True, verbose_name='Shop phone')),
                ('packg_id', models.IntegerField(blank=True, null=True)),
                ('packg_name', models.CharField(blank=True, max_length=100, null=True)),
                ('warranty', models.IntegerField(blank=True, null=True)),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('cust_id', models.IntegerField(blank=True, null=True)),
                ('cust_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Customer Name')),
                ('cust_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Customer address')),
                ('cust_phone', models.IntegerField(blank=True, max_length=100, null=True, verbose_name='Customer phone')),
            ],
        ),
    ]
