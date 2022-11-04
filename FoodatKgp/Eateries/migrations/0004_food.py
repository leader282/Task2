# Generated by Django 4.1.3 on 2022-11-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Eateries", "0003_alter_restaurants_image_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="Food",
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
                ("name", models.CharField(max_length=1000)),
                ("price", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
