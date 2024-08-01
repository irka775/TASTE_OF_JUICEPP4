
from juice_app.models import Category, Recipe
import os
import django
from django.db import connection

# Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "juice_project.settings")

# Initialize Django
django.setup()

# Import models after setting up Django

# Delete all entries from the Category and Recipe tables
Category.objects.all().delete()
Recipe.objects.all().delete()

# Reset auto-increment ID sequences
with connection.cursor() as cursor:
    if connection.vendor == 'postgresql':
        cursor.execute("ALTER SEQUENCE juice_app_category_id_seq "
                       "RESTART WITH 1")
        cursor.execute("ALTER SEQUENCE "
                       "juice_app_recipe_id_seq RESTART WITH 1")
    elif connection.vendor == 'sqlite':
        cursor.execute(
            "DELETE FROM sqlite_sequence WHERE name='juice_app_category'")
        cursor.execute(
            "DELETE FROM sqlite_sequence WHERE name='juice_app_recipe'")

print("All entries deleted and sequences reset.")
