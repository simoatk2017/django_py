# Generated by Django 4.0.4 on 2022-06-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one_to_many', '0002_alter_article1_options_alter_author1_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article1',
            name='category',
            field=models.CharField(choices=[('tech', 'Tech'), ('other', 'Other')], max_length=255),
        ),
    ]
