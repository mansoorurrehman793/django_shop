# Generated by Django 4.2.4 on 2023-12-05 20:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                default=None, max_length=150, null=True, unique=True
            ),
        ),
    ]