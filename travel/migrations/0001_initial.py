# Generated by Django 4.1.2 on 2022-10-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TouristArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('upazilla', models.CharField(max_length=50)),
            ],
        ),
    ]
