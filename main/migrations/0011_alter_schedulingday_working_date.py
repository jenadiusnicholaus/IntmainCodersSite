# Generated by Django 3.2.3 on 2021-06-11 15:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210611_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulingday',
            name='working_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]