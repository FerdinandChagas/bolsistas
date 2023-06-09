# Generated by Django 4.0.10 on 2023-06-26 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frequencias', '0003_projeto_coordenador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequencia',
            name='ch_total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='pontos',
            field=models.ManyToManyField(null=True, related_name='frequencia', to='frequencias.ponto'),
        ),
    ]
