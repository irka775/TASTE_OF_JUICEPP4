from django.contrib import admin
from .models import Category, Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    list_display = ("name", "slug", "description")
    search_fields = ["name"]
    list_filter = ("name", "description")  # Corectare: 'desciption' -> 'description'
    prepopulated_fields = {"slug": ("name",)}
    summernote_fields = ("description",)


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    search_fields = ["title", "content"]
    list_filter = ("status", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


admin.site.register(Comment)
