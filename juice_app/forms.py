"""
Forms for managing user interactions related to comments and recipes.
"""

from django import forms
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    """
    Form for creating and updating comments.
    """

    class Meta:
        model = Comment
        fields = ("body",)  # Only include the 'body' field in the form


class RecipeForm(forms.ModelForm):
    """
    Form for creating and updating recipes.
    """

    class Meta:
        model = Recipe
        fields = [
            "title",
            "category",
            "featured_image",
            "description",
            "ingredients",
            "instructions",
            "status",
        ]
        widgets = {
            "title": forms.TextInput
            (attrs={"class": "form-control form-title"}),       
            "slug": forms.TextInput
            (attrs={"class": "form-control form-title"}),
            "featured_image": forms.ClearableFileInput
            (attrs={"class": "form-control-file form-featured-image"}),

            "description": forms.Textarea
            (attrs={"class": "form-control form-description"}),
            "status": forms.Select
            (attrs={"class": "form-control form-select"}),
            "ingredients": forms.Textarea
            (attrs={"class": "form-control form-ingredients"}),
            "instructions": forms.Textarea
            (attrs={"class": "form-control form-instructions"}),
            "category": forms.Select
            (attrs={"class": "form-control form-select"}),
        }
