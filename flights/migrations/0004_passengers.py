# Generated by Django 5.0.4 on 2024-04-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_rename_city_airport_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passengers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.flights')),
            ],
        ),
    ]
