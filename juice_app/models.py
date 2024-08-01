from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


class Category(models.Model):
    """
    Model representing a category for recipes.
    """

    name: models.CharField = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    featured_image = CloudinaryField("juice_category_image",
                                     default="placeholder")

    def __str__(self):
        return str(self.name)


# Status choices for the Recipe model
STATUS = ((0, "Draft"), (1, "Publish"))


class Recipe(models.Model):
    """
    Model representing a recipe.
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes")
    featured_image = CloudinaryField(
        "juice_recipe_image", default="placeholder")
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="recipes"
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Override the save method to auto-generate the slug from the title
        if it doesn't exist.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Model representing a comment on a recipe.
    """

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]  # Orders comments by most recent first

    def __str__(self):
        # Displays the first 20 characters of the comment body for better
        # readability
        return f"Comment {self.body[:20]} by {self.author}"
