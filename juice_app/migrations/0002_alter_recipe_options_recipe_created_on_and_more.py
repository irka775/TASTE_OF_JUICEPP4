# Generated by Django 4.2.9 on 2024-07-24 09:17

import cloudinary.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("juice_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="recipe",
            options={"ordering": ["created_on"]},
        ),
        migrations.AddField(
            model_name="recipe",
            name="created_on",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="recipe",
            name="featured_image",
            field=cloudinary.models.CloudinaryField(
                default="placeholder", max_length=255, verbose_name="image"
            ),
        ),
        migrations.AddField(
            model_name="recipe",
            name="slug",
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="recipe",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
    ]