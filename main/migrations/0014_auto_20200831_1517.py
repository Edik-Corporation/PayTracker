# Generated by Django 3.1 on 2020-08-31 12:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200829_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 31, 12, 17, 46, 86189, tzinfo=utc), verbose_name='Created Date'),
        ),
    ]
