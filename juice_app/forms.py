from .models import Comment, Recipe
from django import forms


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
            # Custom widget for the 'title' field with a specific CSS class
            "title": forms.TextInput(attrs={"class": "form-control form-title"}),
            # Custom widget for the 'featured_image' field with a specific CSS class
            "featured_image": forms.ClearableFileInput(
                attrs={"class": "form-control-file form-featured-image"}
            ),
            # Custom widget for the 'description' field with a specific CSS class
            "description": forms.Textarea(
                attrs={"class": "form-control form-description"}
            ),
            # Custom widget for the 'status' field with a specific CSS class
            "status": forms.Select(attrs={"class": "form-control form-select"}),
            # Custom widget for the 'ingredients' field with a specific CSS class
            "ingredients": forms.Textarea(
                attrs={"class": "form-control form-ingredients"}
            ),
            # Custom widget for the 'instructions' field with a specific CSS class
            "instructions": forms.Textarea(
                attrs={"class": "form-control form-instructions"}
            ),
            # Custom widget for the 'category' field with a specific CSS class
            "category": forms.Select(attrs={"class": "form-control form-select"}),
        }
