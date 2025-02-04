# Generated by Django 4.1.6 on 2023-02-11 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CelestialObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=250)),
                ('last_appearance', models.DateTimeField()),
                ('discovered_by', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('description', models.TextField(max_length=250)),
                ('celestial_objects', models.ManyToManyField(to='main_app.celestialobject')),
            ],
        ),
    ]
