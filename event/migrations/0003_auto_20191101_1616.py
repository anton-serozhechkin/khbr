# Generated by Django 2.2.6 on 2019-11-01 14:16

from django.db import migrations, models
import event.models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20191101_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(blank=True, verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to=event.models.upload_event_images_folder, verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.CharField(blank=True, max_length=300, verbose_name='Место'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(blank=True, verbose_name='Начало'),
        ),
    ]
