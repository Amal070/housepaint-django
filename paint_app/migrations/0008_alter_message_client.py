# Generated by Django 4.1.2 on 2024-01-11 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paint_app', '0007_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='paint_app.book', verbose_name='client'),
        ),
    ]
