# Generated by Django 2.2.8 on 2020-06-11 13:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200611_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 11, 13, 48, 9, 199590, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 11, 13, 48, 9, 199144, tzinfo=utc)),
        ),
    ]