# Generated by Django 3.2.19 on 2023-06-20 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_remove_new_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='N',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_time', models.CharField(blank=True, max_length=200, null=True)),
                ('ntpserverip', models.CharField(blank=True, max_length=200, null=True)),
                ('stratum', models.BigIntegerField(blank=True, null=True)),
                ('pcip', models.CharField(blank=True, max_length=2, null=True)),
                ('t0', models.DecimalField(blank=True, decimal_places=10, max_digits=250, null=True)),
                ('t1', models.DecimalField(blank=True, decimal_places=10, max_digits=250, null=True)),
                ('t2', models.DecimalField(blank=True, decimal_places=10, max_digits=250, null=True)),
                ('t3', models.DecimalField(blank=True, decimal_places=10, max_digits=250, null=True)),
                ('toffset', models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True)),
                ('tdelay', models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True)),
            ],
        ),
    ]
