# Generated by Django 4.2.3 on 2023-08-27 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("debit", "0002_alter_debit_categoty"),
    ]

    operations = [
        migrations.RenameField(
            model_name="credit",
            old_name="categoty",
            new_name="category",
        ),
        migrations.RenameField(
            model_name="debit",
            old_name="categoty",
            new_name="category",
        ),
    ]
