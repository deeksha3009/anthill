# Generated by Django 2.1.2 on 2018-10-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goals',
            old_name='grp',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='update',
            old_name='grouping',
            new_name='group',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='milestones',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='goals',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
