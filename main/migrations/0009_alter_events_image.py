# Generated by Django 3.2.3 on 2021-06-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='image',
            field=models.FileField(null=True, upload_to='event_files'),
        ),
    ]
