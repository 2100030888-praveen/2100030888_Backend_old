# Generated by Django 5.0.4 on 2024-04-29 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('country_id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=50)),
                ('region_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('location_id', models.IntegerField(primary_key=True, serialize=False)),
                ('street_address', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=30)),
                ('state_province', models.CharField(blank=True, max_length=25, null=True)),
                ('country_id', models.CharField(max_length=2)),
            ],
        ),
    ]
