# Generated by Django 3.2.4 on 2022-09-05 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ks', '0010_ks_pnuh_con_med_ks_pnuh_history'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ks_pnuh_con_med',
            options={'verbose_name': '병용약물', 'verbose_name_plural': '병용약물'},
        ),
        migrations.AlterModelOptions(
            name='ks_pnuh_history',
            options={'verbose_name': '과거 병력', 'verbose_name_plural': '과거 병력'},
        ),
    ]