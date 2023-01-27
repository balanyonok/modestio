# Generated by Django 4.1.5 on 2023-01-26 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0005_rename_photo_cat_photo1_cat_photo2_cat_photo3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='photo1',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='photo2',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='photo3',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='cats.cat')),
            ],
        ),
    ]
