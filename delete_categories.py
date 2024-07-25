import os
import django

# Configurează setările Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'juice_project.settings')
django.setup()

from django.db import connection
from juice_app.models import Category, Recipe

# Șterge toate intrările din tabele
Category.objects.all().delete()
Recipe.objects.all().delete()

# Resetează secvențele ID-urilor auto-increment
with connection.cursor() as cursor:
    cursor.execute("ALTER SEQUENCE juice_app_category_id_seq RESTART WITH 1")
    cursor.execute("ALTER SEQUENCE juice_app_recipe_id_seq RESTART WITH 1")

print("All entries deleted and sequences reset.")
