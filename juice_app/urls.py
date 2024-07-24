from django.urls import path
from . import views

urlpatterns = [
    # ====================================================================
    path("", views.HomePage.as_view(), name="home"),
    path("recipe_list", views.PostList.as_view(), name="recipe_list"),
    # ====================================================================
    path("<slug:slug>/", views.recipe_detail, name="recipe_detail"),
    # ====================================================================
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        views.comment_edit,
        name="comment_edit",
    ),
    # ====================================================================
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        views.comment_delete,
        name="comment_delete",
    ),
    # ====================================================================
]
