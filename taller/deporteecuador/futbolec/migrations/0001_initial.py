# Generated by Django 4.0.5 on 2022-06-14 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_campeonato', models.CharField(max_length=30)),
                ('auspiciante', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CampeonatoEquipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField()),
                ('campeonato_equip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loscampeonatos', to='futbolec.campeonato')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('siglas', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('campeonatos', models.ManyToManyField(through='futbolec.CampeonatoEquipos', to='futbolec.campeonato')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('posicion', models.CharField(max_length=30)),
                ('numero_camiseta', models.IntegerField()),
                ('sueldo', models.IntegerField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='losequipos', to='futbolec.equipo')),
            ],
        ),
        migrations.AddField(
            model_name='campeonatoequipos',
            name='equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loscampeonatos', to='futbolec.equipo'),
        ),
        migrations.AddField(
            model_name='campeonato',
            name='equipos',
            field=models.ManyToManyField(through='futbolec.CampeonatoEquipos', to='futbolec.equipo'),
        ),
    ]