# Generated by Django 2.1.2 on 2018-10-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0006_auto_20181022_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='invites',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
