# Generated by Django 4.1.2 on 2024-01-11 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paint_app', '0006_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
