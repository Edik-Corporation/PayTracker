# Generated by Django 3.1 on 2020-09-20 06:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20200919_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 20, 6, 39, 59, 471945, tzinfo=utc), verbose_name='Created Date'),
        ),
    ]