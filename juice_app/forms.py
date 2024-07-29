from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)


class RecipeForm(forms.ModelForm):
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
            "title": forms.TextInput(attrs={"class": "form-control form-title"}),
            "featured_image": forms.ClearableFileInput(
                attrs={"class": "form-control-file form-featured-image"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control form-description"}
            ),
            "status": forms.Select(attrs={"class": "form-control form-select"}),
            "ingredients": forms.Textarea(
                attrs={"class": "form-control form-ingredients"}
            ),
            "instructions": forms.Textarea(
                attrs={"class": "form-control form-instructions"}
            ),
            "category": forms.Select(attrs={"class": "form-control form-select"}),
        }
