# Generated by Django 3.2.9 on 2021-12-01 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=55)),
                ('imagen_escudo', models.ImageField(blank=True, null=True, upload_to='equipo')),
                ('year_fundacion', models.IntegerField()),
            ],
            options={
                'verbose_name': 'equipo',
                'verbose_name_plural': 'equipos',
            },
        ),
        migrations.CreateModel(
            name='Plantilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_jugador', models.CharField(max_length=55)),
                ('imagen_jugador', models.ImageField(blank=True, null=True, upload_to='plantilla')),
                ('position_jugador', models.CharField(max_length=55)),
                ('dorsal', models.IntegerField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipos_futbol_app.equipo')),
            ],
            options={
                'verbose_name': 'plantilla',
                'verbose_name_plural': 'plantillas',
            },
        ),
    ]
