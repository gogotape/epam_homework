# Generated by Django 3.2.4 on 2021-06-20 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sqldata", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homework",
            name="created",
            field=models.DateTimeField(verbose_name="When was created"),
        ),
    ]