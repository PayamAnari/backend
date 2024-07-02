# Generated by Django 5.0.2 on 2024-06-29 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_property_favorited'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending', max_length=10),
        ),
    ]