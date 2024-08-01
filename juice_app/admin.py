from django.contrib import admin
from .models import Category, Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Category model.
    Uses Summernote for rich text editing of the description field.
    """

    # Fields to display in the admin list view
    list_display = ("name", "slug", "description")
    # Fields to include in the admin search
    search_fields = ["name"]
    # Fields to filter by in the admin list view
    list_filter = ("name", "description")
    prepopulated_fields = {
        "slug": ("name",)
    }  # Automatically populate the slug field from the name
    summernote_fields = (
        "description",
    )  # Use Summernote widget for the description field


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Recipe model.
    Uses Summernote for rich text editing of the content field.
    """

    list_display = (
        "title",
        "slug",
        "status",
        "created_on",
    )  # Fields to display in the admin list view
    # Fields to include in the admin search
    search_fields = ["title", "content"]
    # Fields to filter by in the admin list view
    list_filter = ("status", "created_on")
    prepopulated_fields = {
        "slug": ("title",)
    }  # Automatically populate the slug field from the title
    # Use Summernote widget for the content field
    summernote_fields = ("content",)


# Register the Comment model in the admin site without custom configuration
admin.site.register(Comment)
