# Generated by Django 4.0.10 on 2023-06-25 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=150)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ProReitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio_m', models.DateField(null=True)),
                ('fim_m', models.DateField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orientador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacao', models.CharField(max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('endereco', models.CharField(max_length=150)),
                ('responsavel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campus', to='users.coordenador')),
            ],
        ),
        migrations.CreateModel(
            name='Bolsista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.campus')),
                ('orientador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bolsistas', to='users.orientador')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.projeto')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]