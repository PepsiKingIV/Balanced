# Generated by Django 4.2.3 on 2023-08-31 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="number_of_emails",
            field=models.IntegerField(default=0),
        ),
    ]
