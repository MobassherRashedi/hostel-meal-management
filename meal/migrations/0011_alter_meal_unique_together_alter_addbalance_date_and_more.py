# Generated by Django 4.0.3 on 2022-03-30 07:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0010_totalexpenses_amount_totalexpenses_created_date_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='meal',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='addbalance',
            name='date',
            field=models.DateField(default=datetime.date(2022, 3, 30)),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2022, 3, 30), null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateField(default=datetime.date(2022, 3, 30)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.date(2022, 3, 30)),
        ),
        migrations.AddConstraint(
            model_name='expenses',
            constraint=models.UniqueConstraint(fields=('date', 'user'), name='user_unique_day_expense'),
        ),
    ]
