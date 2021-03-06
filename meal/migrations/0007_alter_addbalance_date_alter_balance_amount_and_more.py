# Generated by Django 4.0.3 on 2022-03-29 08:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0006_balance_addbalance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbalance',
            name='date',
            field=models.DateField(default=datetime.date(2022, 3, 29)),
        ),
        migrations.AlterField(
            model_name='balance',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9999),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.date(2022, 3, 29)),
        ),
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateField(default=datetime.date(2022, 3, 29)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.date(2022, 3, 29)),
        ),
    ]
