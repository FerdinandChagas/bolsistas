# Generated by Django 4.0.10 on 2023-06-26 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frequencias', '0005_remove_frequencia_pontos_ponto_bolsista_and_more'),
        ('users', '0009_remove_bolsista_pontos'),
    ]

    operations = [
        migrations.AddField(
            model_name='orientador',
            name='campus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orientadores', to='frequencias.campus'),
        ),
    ]
