# Generated by Django 4.1.7 on 2023-08-17 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('website', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=0)),
                ('service_speed', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('menu', models.CharField(max_length=200)),
            ],
        ),
    ]
