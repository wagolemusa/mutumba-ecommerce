# Generated by Django 2.2.16 on 2021-01-21 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0008_auto_20210120_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
