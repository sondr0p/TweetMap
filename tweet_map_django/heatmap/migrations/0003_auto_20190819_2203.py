# Generated by Django 2.2.4 on 2019-08-19 22:03

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heatmap', '0002_auto_20190819_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='hashtag',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='tweet',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='hashtag',
        ),
        migrations.AddField(
            model_name='tweet',
            name='hashtags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, size=None),
        ),
        migrations.DeleteModel(
            name='Hashtag',
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
    ]