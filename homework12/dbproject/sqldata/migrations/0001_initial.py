# Generated by Django 3.2.4 on 2021-06-20 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Homework",
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
                ("text", models.CharField(max_length=250, verbose_name="Text")),
                ("deadline", models.DateTimeField(blank=True, verbose_name="Deadline")),
                (
                    "created",
                    models.DateTimeField(blank=True, verbose_name="When was created"),
                ),
                ("time", models.CharField(default="timezone.now", max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("last_name", models.CharField(max_length=250, verbose_name="Surname")),
                ("first_name", models.CharField(max_length=250, verbose_name="Name")),
                ("new_value", models.CharField(max_length=250, verbose_name="Name")),
            ],
        ),
        migrations.CreateModel(
            name="Teacher",
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
                ("last_name", models.CharField(max_length=250, verbose_name="Surname")),
                ("first_name", models.CharField(max_length=250, verbose_name="Name")),
            ],
        ),
        migrations.CreateModel(
            name="HomeworkResult",
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
                ("solution", models.CharField(max_length=250, verbose_name="Solution")),
                ("created", models.DateTimeField(verbose_name="When was created")),
                ("time", models.CharField(default="timezone.now", max_length=250)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sqldata.student",
                    ),
                ),
                (
                    "homework",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sqldata.homework",
                    ),
                ),
            ],
        ),
    ]
