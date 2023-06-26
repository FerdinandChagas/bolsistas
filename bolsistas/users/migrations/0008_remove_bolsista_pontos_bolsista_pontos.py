# Generated by Django 4.0.10 on 2023-06-26 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frequencias', '0004_alter_frequencia_ch_total_alter_frequencia_pontos'),
        ('users', '0007_alter_bolsista_orientador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bolsista',
            name='pontos',
        ),
        migrations.AddField(
            model_name='bolsista',
            name='pontos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bolsista', to='frequencias.ponto'),
        ),
    ]
