# Generated by Django 3.2.7 on 2021-10-04 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0003_auto_20211004_2002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery',
            old_name='Parcel',
            new_name='parcel',
        ),
    ]
