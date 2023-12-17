# Generated by Django 3.2.19 on 2023-05-24 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_new'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='tag',
            new_name='errmsg',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='count',
            new_name='iserror',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='index',
            new_name='t0',
        ),
        migrations.AddField(
            model_name='new',
            name='ntpserverip',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='pcip',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='stratum',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='t1',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='t2',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='t3',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='tdelay',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=25, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='toffset',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=25, null=True),
        ),
    ]
