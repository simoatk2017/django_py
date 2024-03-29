# Generated by Django 4.0.4 on 2022-06-24 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0005_alter_employee_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contactApp.employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='repair',
            name='car',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contactApp.car'),
            preserve_default=False,
        ),
    ]
