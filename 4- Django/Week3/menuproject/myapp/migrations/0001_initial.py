# Generated by Django 4.2 on 2023-04-05 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cusine', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]