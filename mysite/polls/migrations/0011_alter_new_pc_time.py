# Generated by Django 3.2.19 on 2023-06-07 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20230601_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='pc_time',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
