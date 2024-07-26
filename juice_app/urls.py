from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("add_juice/", views.add_juice, name="add_juice"),
    path("recipe_list/", views.recipe_list, name="recipe_list"),
    path("recipe_list/edit_recipe/<int:recipe_id>/", views.recipe_edit, name="recipe_edit"),
    path("recipe_list/delete_recipe/<int:recipe_id>/", views.recipe_delete, name="recipe_delete"),
    path("<slug:slug>/edit_comment/<int:comment_id>/", views.comment_edit, name="comment_edit"),
    path("<slug:slug>/delete_comment/<int:comment_id>/", views.comment_delete, name="comment_delete"),
    path("<slug:slug>/", views.recipe_detail, name="recipe_detail"),
]
