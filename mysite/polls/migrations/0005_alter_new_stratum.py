# Generated by Django 3.2.19 on 2023-05-24 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20230524_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='stratum',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]