# Generated by Django 3.2.12 on 2022-04-22 12:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0005_create_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 24, 12, 15, 9, 135944, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
