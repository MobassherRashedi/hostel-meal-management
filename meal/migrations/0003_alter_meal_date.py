# Generated by Django 4.0.3 on 2022-03-25 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0002_remove_product_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateField(default=datetime.date(2022, 3, 25), unique=True),
        ),
    ]
