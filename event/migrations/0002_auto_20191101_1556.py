# Generated by Django 2.2.6 on 2019-11-01 13:56

from django.db import migrations, models
import event.models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.DateField(verbose_name='День события'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to=event.models.upload_event_images_folder, verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='event',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Заметки'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(verbose_name='Начало'),
        ),
    ]
