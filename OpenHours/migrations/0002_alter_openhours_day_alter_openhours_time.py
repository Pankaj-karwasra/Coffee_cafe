# Generated by Django 4.1.5 on 2023-09-19 07:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("OpenHours", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="openhours",
            name="day",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="openhours",
            name="time",
            field=models.CharField(max_length=100),
        ),
    ]
