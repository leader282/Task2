# Generated by Django 4.1.3 on 2022-11-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Eateries", "0005_restaurants_menu"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurants",
            name="menu",
            field=models.ManyToManyField(related_name="menu", to="Eateries.food"),
        ),
    ]
