# Generated by Django 3.2.8 on 2022-11-06 23:29

from django.db import migrations, models

from account.models import UserAccount


class Migration(migrations.Migration):
    def add_admin(apps, schema_editor):
        admin = UserAccount.objects.create_user("admin", "admin@gmail.com", "password")
        admin.first_name = "admin"
        admin.last_name = " "
        admin.setManager()
        admin.store = True
        admin.funds = 1000
        admin.save()

    def add_emp(apps, schema_editor):
        emp = UserAccount.objects.create_user("demoemp", "demoemp@gmail.com", "password")
        emp.first_name = "demo"
        emp.last_name = "emp"
        emp.setEmployee()
        emp.store = False
        emp.funds = 50
        emp.save()

    def add_cust(apps, schema_editor):
        cust = UserAccount.objects.create_user("democustomer", "democustomer@gmail.com", "password")
        cust.first_name = "demo"
        cust.last_name = "customer"
        cust.setCustomer()
        cust.store = False
        cust.funds = 50
        cust.save()


    dependencies = [
        ('account', '0009_alter_useraccount_funds_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='store',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(add_admin),
        migrations.RunPython(add_emp),
        migrations.RunPython(add_cust),
    ]
