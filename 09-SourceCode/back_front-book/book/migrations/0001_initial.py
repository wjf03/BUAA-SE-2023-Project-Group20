# Generated by Django 4.2.2 on 2023-06-08 03:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("book_id", models.AutoField(primary_key=True, serialize=False)),
                ("book_name", models.CharField(max_length=20)),
                ("book_introduction", models.CharField(max_length=100)),
                ("book_main_type", models.CharField(max_length=50)),
                ("book_secondary_type", models.CharField(max_length=50)),
                ("book_author_name", models.CharField(default="", max_length=20)),
                ("book_popularity", models.IntegerField()),
                (
                    "book_score",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(5),
                            django.core.validators.MinValueValidator(0),
                        ]
                    ),
                ),
                ("book_url", models.CharField(default="null", max_length=100)),
            ],
        ),
    ]
