# Generated by Django 4.2.4 on 2023-09-30 14:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="available_quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]
