# Generated by Django 4.2.3 on 2023-08-27 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("debit", "0003_rename_categoty_credit_category_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="debit",
            new_name="data",
        ),
    ]
