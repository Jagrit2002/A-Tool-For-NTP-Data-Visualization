# Generated by Django 3.2.19 on 2023-06-19 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_new_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='Img',
        ),
    ]
