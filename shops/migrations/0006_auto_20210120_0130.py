# Generated by Django 2.2.16 on 2021-01-20 01:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0005_auto_20210117_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='county',
        ),
        migrations.RemoveField(
            model_name='billingaddress',
            name='zip',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
