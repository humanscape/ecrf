# Generated by Django 3.2.4 on 2022-07-11 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ks', '0003_auto_20220610_1625'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ks_amc',
        ),
        migrations.DeleteModel(
            name='Ks_cbnuh',
        ),
        migrations.DeleteModel(
            name='Ks_knuh',
        ),
        migrations.DeleteModel(
            name='Ks_smc',
        ),
    ]
