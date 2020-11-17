# Generated by Django 3.1 on 2020-11-17 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Url')),
                ('purchases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.purchase')),
            ],
            options={
                'verbose_name': 'Statistics',
                'verbose_name_plural': 'Statistics',
            },
        ),
    ]
