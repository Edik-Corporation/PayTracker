# Generated by Django 3.1 on 2020-08-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_purchase_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateField(default='26.08.2020"'),
        ),
    ]