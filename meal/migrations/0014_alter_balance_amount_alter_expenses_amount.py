# Generated by Django 4.0.3 on 2022-04-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0013_alter_addbalance_date_alter_balance_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
