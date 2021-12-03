# Generated by Django 3.2.9 on 2021-12-03 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Equipos_futbol_app', '0004_auto_20211203_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantilla',
            name='pais',
            field=models.CharField(blank=True, default=1, max_length=55),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Trofeos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copa_rey', models.IntegerField()),
                ('copa_liga', models.IntegerField()),
                ('copa_europa', models.IntegerField()),
                ('copa_uefa', models.IntegerField()),
                ('equipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Equipos_futbol_app.equipo')),
            ],
            options={
                'verbose_name': 'trofeo',
                'verbose_name_plural': 'trofeos',
            },
        ),
    ]
