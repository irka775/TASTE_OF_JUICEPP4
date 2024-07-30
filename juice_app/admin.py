from django.contrib import admin
from .models import Category, Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Category model.
    Uses Summernote for rich text editing of the description field.
    """
    list_display = ("name", "slug", "description")  # Fields to display in the admin list view
    search_fields = ["name"]  # Fields to include in the admin search
    list_filter = ("name", "description")  # Fields to filter by in the admin list view
    prepopulated_fields = {"slug": ("name",)}  # Automatically populate the slug field from the name
    summernote_fields = ("description",)  # Use Summernote widget for the description field


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Recipe model.
    Uses Summernote for rich text editing of the content field.
    """
    list_display = ("title", "slug", "status", "created_on")  # Fields to display in the admin list view
    search_fields = ["title", "content"]  # Fields to include in the admin search
    list_filter = ("status", "created_on")  # Fields to filter by in the admin list view
    prepopulated_fields = {"slug": ("title",)}  # Automatically populate the slug field from the title
    summernote_fields = ("content",)  # Use Summernote widget for the content field


# Register the Comment model in the admin site without custom configuration
admin.site.register(Comment)
