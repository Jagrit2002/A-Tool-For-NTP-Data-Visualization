# Generated by Django 3.2.19 on 2023-06-20 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_n_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='n',
            name='t0',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=250, null=True),
        ),
        migrations.AlterField(
            model_name='n',
            name='t1',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=250, null=True),
        ),
        migrations.AlterField(
            model_name='n',
            name='t2',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=250, null=True),
        ),
        migrations.AlterField(
            model_name='n',
            name='t3',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=250, null=True),
        ),
    ]
