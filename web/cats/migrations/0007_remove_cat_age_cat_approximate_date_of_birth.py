# Generated by Django 4.1.5 on 2023-01-27 14:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0006_remove_cat_photo1_remove_cat_photo2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='age',
        ),
        migrations.AddField(
            model_name='cat',
            name='approximate_date_of_birth',
            field=models.DateField(default=datetime.date(1900, 1, 1)),
        ),
    ]
