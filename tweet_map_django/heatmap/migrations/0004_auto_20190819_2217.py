# Generated by Django 2.2.4 on 2019-08-19 22:17

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heatmap', '0003_auto_20190819_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='hashtags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100, null=True), null=True, size=None),
        ),
    ]
