# Generated by Django 4.0.2 on 2022-11-08 06:32

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_useraccount_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='cart',
            field=models.JSONField(default=account.models.UserAccount.get_empty_order),
        ),
    ]
