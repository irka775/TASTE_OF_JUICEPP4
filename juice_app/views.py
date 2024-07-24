from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Recipe
from .forms import RecipeForm
from django.views import View

class IndexView(TemplateView):
    """
    View to display home page.
    """
    template_name = "juice_app/index.html"

@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            messages.success(request, 'Recipe created successfully!')
            return redirect('recipe_list')  # Assume you have a recipe list view
    else:
        form = RecipeForm()
    return render(request, 'juice_app/create_recipe.html', {'form': form})

@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recipe updated successfully!')
            return redirect('recipe_list')  # Assume you have a recipe list view
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'edit_recipe.html', {'form': form})


class RecipeListView(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        return render(request, 'juice_app/recipe_list.html', {'recipes': recipes})

# Or use a function-based view
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'juice_app/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, 'juice_app/recipe_detail.html', {'recipe': recipe})
