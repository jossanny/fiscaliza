# Generated by Django 5.1.6 on 2025-02-14 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fiscalizacaobrd_app", "0003_fiscalizacao_offline_id_alter_fiscalizacao_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fiscalizacao",
            name="offline_id",
        ),
        migrations.AlterField(
            model_name="fiscalizacao",
            name="area_medicao_ha",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="fiscalizacao",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
