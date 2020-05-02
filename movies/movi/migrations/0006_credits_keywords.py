# Generated by Django 2.1.4 on 2020-04-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movi', '0005_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cast', models.CharField(blank=True, max_length=2000)),
                ('crew', models.CharField(blank=True, max_length=2000)),
                ('idd', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idd', models.CharField(blank=True, max_length=20)),
                ('keywords', models.CharField(blank=True, max_length=2000)),
            ],
        ),
    ]
