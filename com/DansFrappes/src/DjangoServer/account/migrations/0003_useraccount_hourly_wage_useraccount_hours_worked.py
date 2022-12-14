# Generated by Django 4.0.2 on 2022-10-31 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'), ('account', '0002_useraccount_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='hourly_wage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='hours_worked',
            field=models.SmallIntegerField(default=0),
        ),
    ]