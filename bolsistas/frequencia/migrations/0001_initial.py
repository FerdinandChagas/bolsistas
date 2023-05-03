# Generated by Django 4.2 on 2023-04-28 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bolsista",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("matricula", models.IntegerField()),
                ("curso", models.CharField(max_length=140)),
                ("periodo", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Registro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hora_entrada", models.TimeField()),
                ("hora_saida", models.TimeField()),
                ("data", models.DateField()),
                ("carga_horaria", models.IntegerField()),
                (
                    "bolsista",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="frequencia.bolsista",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Orientador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("matricula", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                (
                    "bolsistas",
                    models.ManyToManyField(
                        blank=True, related_name="orientador", to="frequencia.bolsista"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Frequencia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mes", models.CharField(max_length=20)),
                ("carga_horaria_total", models.IntegerField()),
                (
                    "bolsista",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="frequencia.bolsista",
                    ),
                ),
                (
                    "registros",
                    models.ManyToManyField(blank=True, to="frequencia.registro"),
                ),
            ],
        ),
    ]
