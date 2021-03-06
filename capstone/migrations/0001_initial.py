# Generated by Django 2.1.2 on 2018-10-21 09:25

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('is_done', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=15)),
                ('no_of_members', models.IntegerField(null=True)),
                ('no_of_guides', models.IntegerField(null=True)),
                ('members', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), size=None)),
                ('guide', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Milestones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, null=True)),
                ('content', models.TextField(max_length=150, null=True)),
                ('due_date', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='capstone.Group')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('category', models.CharField(choices=[('ADMIN', 'admin'), ('USER', 'member'), ('GUIDE', 'guide')], default='ADMIN', max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=' ')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('text', models.TextField(max_length=150)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('grouping', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='capstone.Group')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='goals',
            name='grp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='capstone.Group'),
        ),
        migrations.AddField(
            model_name='goals',
            name='link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='capstone.Milestones'),
        ),
    ]
