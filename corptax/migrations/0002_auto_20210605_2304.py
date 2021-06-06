# Generated by Django 3.1.12 on 2021-06-05 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eveonline', '0014_auto_20210105_1413'),
        ('corptax', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='corptaxowed',
            old_name='corp_id',
            new_name='corp',
        ),
        migrations.RenameField(
            model_name='corptaxrate',
            old_name='corp_id',
            new_name='corp',
        ),
        migrations.AlterUniqueTogether(
            name='corptaxowed',
            unique_together={('corp', 'month')},
        ),
        migrations.AlterUniqueTogether(
            name='corptaxrate',
            unique_together={('corp', 'date')},
        ),
    ]
