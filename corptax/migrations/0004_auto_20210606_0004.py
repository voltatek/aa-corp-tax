# Generated by Django 3.1.12 on 2021-06-06 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corptax', '0003_auto_20210605_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corptaxowed',
            name='month',
            field=models.DateField(),
        ),
    ]
