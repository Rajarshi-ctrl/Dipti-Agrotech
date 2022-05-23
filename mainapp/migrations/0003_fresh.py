# Generated by Django 4.0 on 2022-05-09 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_contact_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fresh',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=200)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
            ],
        ),
    ]