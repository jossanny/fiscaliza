# Generated by Django 5.1.6 on 2025-02-13 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "fiscalizacaobrd_app",
            "0002_rename_fiscal_campo_fiscalizacao_fiscal_responsavel",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="fiscalizacao",
            name="offline_id",
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="fiscalizacao",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
