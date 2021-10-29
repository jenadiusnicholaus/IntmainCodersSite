# Generated by Django 3.2.3 on 2021-06-13 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210613_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulingday',
            name='scheduling_class',
            field=models.ManyToManyField(related_name='list_of_class_per_day', to='main.SchedulingClass'),
        ),
        migrations.DeleteModel(
            name='assignClassToDay',
        ),
    ]
