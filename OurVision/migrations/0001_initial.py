# Generated by Django 4.1.5 on 2023-09-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OurVision",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("desciption", models.TextField()),
                ("title1", models.TextField()),
                ("title2", models.TextField()),
                ("title3", models.TextField()),
            ],
        ),
    ]