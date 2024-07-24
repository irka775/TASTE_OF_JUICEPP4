from django.urls import path
from . import views
from .views import IndexView, recipe_list, RecipeListView

urlpatterns = [
    path('create-recipe/', views.create_recipe, name='create_recipe'),
    path('edit-recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('', IndexView.as_view(), name='index'),
]
