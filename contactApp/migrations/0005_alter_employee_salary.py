# Generated by Django 4.0.4 on 2022-06-24 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0004_car_employee_repair'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]