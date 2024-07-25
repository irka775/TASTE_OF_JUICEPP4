from django.urls import path
from . import views
from .views import add_juice

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("add_juice/", add_juice, name="add_juice"),
    path("recipe_list/", views.recipe_list, name="recipe_list"),
    path("<slug:slug>/edit_comment/<int:comment_id>/", views.comment_edit, name="comment_edit"),
    path("<slug:slug>/delete_comment/<int:comment_id>/", views.comment_delete, name="comment_delete"),
    path("<slug:slug>/", views.recipe_detail, name="recipe_detail"),
]
