# Generated by Django 3.2.7 on 2021-09-30 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characteristic', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characteristic_value', models.CharField(max_length=100)),
            ],
        ),
    ]
