# Generated by Django 4.2.3 on 2023-08-30 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("debit", "0007_alter_credit_id_alter_data_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="credit",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="data",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]