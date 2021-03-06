# Generated by Django 3.1 on 2020-08-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('about', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('about_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
