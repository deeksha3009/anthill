# Generated by Django 2.1.2 on 2018-10-23 06:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0012_auto_20181023_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='guide',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='group',
            name='members',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), blank=True, default=list, size=None),
        ),
    ]
