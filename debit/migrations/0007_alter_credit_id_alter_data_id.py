# Generated by Django 4.2.3 on 2023-08-30 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("debit", "0006_alter_data_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="credit",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="data",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
