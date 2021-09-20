# Generated by Django 3.2.7 on 2021-09-20 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CourierShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_begin', models.DateField()),
                ('shift_end', models.DateField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miare.area')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miare.courier')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miare.shift')),
            ],
        ),
        migrations.CreateModel(
            name='Capacity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('capacity', models.PositiveIntegerField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miare.area')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miare.shift')),
            ],
            options={
                'verbose_name_plural': 'Capacities',
                'unique_together': {('shift', 'area', 'date')},
            },
        ),
    ]
