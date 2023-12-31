# Generated by Django 4.2.7 on 2023-11-09 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=250)),
                ('recipe_description', models.TextField()),
                ('recipe_image', models.ImageField(upload_to='recipic_image')),
            ],
        ),
    ]
