from juice_app.models import Category, Recipe
from django.db import connection
import os
import django

# Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "juice_project.settings")
django.setup()


# Delete all entries from the Category and Recipe tables
Category.objects.all().delete()
Recipe.objects.all().delete()

# Reset auto-increment ID sequences
with connection.cursor() as cursor:
    cursor.execute("ALTER SEQUENCE juice_app_category_id_seq RESTART WITH 1")
    cursor.execute("ALTER SEQUENCE juice_app_recipe_id_seq RESTART WITH 1")

print("All entries deleted and sequences reset.")
