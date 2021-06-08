# Generated by Django 3.2.3 on 2021-06-05 11:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_schedulingclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulingclass',
            name='ending_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='schedulingclass',
            name='ending_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]