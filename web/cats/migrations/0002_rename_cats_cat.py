# Generated by Django 4.1.5 on 2023-01-26 17:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cats", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Cats",
            new_name="Cat",
        ),
    ]
