from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the home page, which uses a class-based view
    path("", views.HomePage.as_view(), name="home"),
    
    # URL pattern for adding a new juice recipe, which uses a function-based view
    path("add_juice/", views.add_juice, name="add_juice"),
    
    # URL pattern for the list of recipes, which uses a function-based view
    path("recipe_list/", views.recipe_list, name="recipe_list"),
    
    # URL pattern for editing a recipe, which uses a function-based view and includes a slug for the recipe
    path("recipe/<slug:slug>/edit/", views.recipe_edit, name="recipe_edit"),
    
    # URL pattern for deleting a recipe via AJAX, which uses a function-based view and includes a slug for the recipe
    path("recipe/<slug:slug>/delete/", views.ajax_delete_recipe, name="recipe_delete"),
    
    # URL pattern for AJAX search functionality, which uses a function-based view
    path("ajax_search/", views.ajax_search, name="ajax_search"),
    
    # URL pattern for editing a comment, which uses a function-based view and includes a slug for the recipe and an ID for the comment
    path("<slug:slug>/edit_comment/<int:comment_id>/", views.comment_edit, name="comment_edit"),
    
    # URL pattern for deleting a comment, which uses a function-based view and includes a slug for the recipe and an ID for the comment
    path("<slug:slug>/delete_comment/<int:comment_id>/", views.comment_delete, name="comment_delete"),
    
    # URL pattern for viewing the details of a recipe, which uses a function-based view and includes a slug for the recipe
    path("<slug:slug>/", views.recipe_detail, name="recipe_detail"),
]