# Generated by Django 4.2.4 on 2023-09-14 07:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="subcategories",
            old_name="categories_id",
            new_name="categories",
        ),
    ]
