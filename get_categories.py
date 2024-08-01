import os
import django

# Configurează setările Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "juice_project.settings")
django.setup()

from juice_app.models import Category

for category in Category.objects.all():
    print(f"Category: {category.name}, ID: {category.id}")
