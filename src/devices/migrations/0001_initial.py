# Generated by Django 4.2.1 on 2023-07-09 18:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('active', models.BooleanField(default=False)),
                ('website', models.URLField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True)),
                ('city', models.CharField(choices=[('poz', 'Poznań'), ('now', 'Nowhere')])),
                ('street', models.CharField(choices=[('rze', 'os. Rzeczypospolitej'), ('now', 'Nowhere')])),
                ('zip_code', models.CharField(validators=[django.core.validators.RegexValidator('^[0-9]+[0-9]+\\-[0-9]+[0-9]+[0-9]+$', 'IP address should be numeric.')])),
                ('house_number', models.CharField()),
                ('flat_number', models.IntegerField(blank=True, null=True)),
                ('rooms', models.ManyToManyField(to='devices.room')),
            ],
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('api_url', models.URLField(blank=True, null=True)),
                ('type', models.CharField(choices=[('the', 'Thermal'), ('hum', 'Humidity'), ('tah', 'Thermal and Humidity')])),
                ('active', models.BooleanField(default=True)),
                ('ip_address', models.CharField(validators=[django.core.validators.RegexValidator('^[0-9]+[0-9]?[0-9]?\\.[0-9]+[0-9]?[0-9]?\\.[0-9]+[0-9]?[0-9]?\\.[0-9]+[0-9]?[0-9]?$', "IP address should be numeric like '0.0.0.0'.")])),
                ('port', models.IntegerField()),
                ('protocol', models.CharField(choices=[('http', 'http')], default='http')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='devices.house')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.producers')),
            ],
            options={
                'ordering': ('type',),
            },
        ),
    ]
