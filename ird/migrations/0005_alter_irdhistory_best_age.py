# Generated by Django 3.2.4 on 2022-04-21 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ird', '0004_auto_20220421_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='irdhistory',
            name='best_age',
            field=models.TextField(blank=True, help_text='시력이 가장 좋았던 때는 언제인가요?', null=True, verbose_name='가장 좋았을 때 시력 나이'),
        ),
    ]
