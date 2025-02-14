# Generated by Django 5.1.6 on 2025-02-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fiscalizacaobrd_app", "0006_alter_fiscalizacao_area_medicao_ha"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fiscalizacao",
            name="area_medicao_ha",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
