# Generated by Django 3.2.3 on 2021-06-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210613_0737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignclasstoday',
            name='scheduling_class',
        ),
        migrations.AddField(
            model_name='assignclasstoday',
            name='scheduling_class',
            field=models.ManyToManyField(related_name='list_of_class_per_day', to='main.SchedulingClass'),
        ),
    ]