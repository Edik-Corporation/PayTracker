# Generated by Django 3.1 on 2020-09-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200919_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='C:/Users/Alexey/Documents/Django projects/PayTracker/media/avatars/nophoto.jpg', upload_to='avatars', verbose_name='Avatar'),
        ),
    ]
