# Generated by Django 4.0.10 on 2023-06-25 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frequencias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ponto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora_entrada', models.TimeField()),
                ('hora_saida', models.TimeField()),
            ],
            options={
                'verbose_name': 'Ponto',
                'verbose_name_plural': 'Pontos',
            },
        ),
        migrations.AlterModelOptions(
            name='campus',
            options={'verbose_name': 'Campus', 'verbose_name_plural': 'Campus'},
        ),
        migrations.AlterModelOptions(
            name='projeto',
            options={'verbose_name': 'Projeto', 'verbose_name_plural': 'Projetos'},
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=100)),
                ('ch_total', models.FloatField()),
                ('pontos', models.ManyToManyField(related_name='frequencia', to='frequencias.ponto')),
            ],
            options={
                'verbose_name': 'Frequencia',
                'verbose_name_plural': 'Frequencias',
            },
        ),
    ]
