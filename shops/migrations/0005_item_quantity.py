# Generated by Django 2.0.13 on 2020-03-20 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0004_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
