# Generated by Django 3.1 on 2020-09-04 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='md',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
