# Generated by Django 3.1 on 2020-08-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=900)),
            ],
        ),
    ]
