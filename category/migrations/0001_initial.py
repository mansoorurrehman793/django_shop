# Generated by Django 4.2.4 on 2023-09-14 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categories",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(default=None, max_length=100)),
                ("description", models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name="SubCategories",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "categories_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sub_categories",
                        to="category.categories",
                    ),
                ),
            ],
        ),
    ]
