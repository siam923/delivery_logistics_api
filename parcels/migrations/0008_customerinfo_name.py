# Generated by Django 3.2.8 on 2021-10-06 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0007_auto_20211005_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerinfo',
            name='name',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]