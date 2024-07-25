# Generated by Django 4.2.9 on 2024-07-25 17:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("juice_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="featured_image",
            field=cloudinary.models.CloudinaryField(
                default="placeholder",
                max_length=255,
                verbose_name="juice_category_image",
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="featured_image",
            field=cloudinary.models.CloudinaryField(
                default="placeholder", max_length=255, verbose_name="juice_recipe_image"
            ),
        ),
    ]
