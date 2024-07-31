from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .models import Recipe, Comment, Category
from .forms import CommentForm, RecipeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from juice_project.settings import DEBUG


def ajax_search(request):
    """
    Handles AJAX search requests to filter recipes based on query parameters.
    Returns a JSON response with search results.
    """
    query = request.GET.get("q", "")
    recipes = (
        Recipe.objects.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(ingredients__icontains=query)
            | Q(instructions__icontains=query)
        )
        if query
        else Recipe.objects.all()
    )

    results = []
    for recipe in recipes:
        results.append(
            {
                "title": recipe.title,
                "url": reverse("recipe_detail", args=[recipe.slug]),
                "image": recipe.featured_image.url if recipe.featured_image else "",
            }
        )

    return JsonResponse({"results": results})


def ajax_delete_recipe(request, slug):
    """
    Handles AJAX requests to delete a recipe.
    Only allows deletion if the current user is the author of the recipe.
    """
    if request.method == "POST":
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.author == request.user:
            recipe.delete()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False}, status=403)
    return JsonResponse({"success": False}, status=405)


@login_required
def recipe_edit(request, slug):
    """
    Handles editing an existing recipe.
    Only accessible to authenticated users and updates the recipe if the form is valid.
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            messages.success(request, "Recipe updated successfully!")
            return redirect("recipe_list")
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "juice_app/add_juice.html", {"form": form})


@login_required
def recipe_delete(request, slug):
    """
    Handles the deletion of a recipe.
    Only accessible via POST request and displays a confirmation page.
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == "POST":
        recipe.delete()
        messages.success(request, "Recipe deleted successfully!")
        return redirect("recipe_list")
    return render(request, "juice_app/recipe_confirm_delete.html", {"recipe": recipe})


class HomePage(generic.ListView):
    """
    Displays a list of recipes with status=1 on the homepage.
    """

    queryset = Recipe.objects.filter(status=1)
    template_name = "juice_app/index.html"


@login_required
def add_juice(request):
    """
    Handles adding a new recipe.
    Only accessible to authenticated users and saves the new recipe if the form is valid.
    """
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, "Recipe added successfully!")
            return redirect("recipe_detail", slug=recipe.slug)
    else:
        form = RecipeForm()
    return render(request, "juice_app/add_juice.html", {"form": form})


@login_required
def book_new(request):
    """
    Handles adding a new recipe for book creation.
    This function seems similar to `add_juice` and saves the new recipe if the form is valid.
    """
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            messages.success(request, "Recipe added successfully!")
            return redirect("recipe_detail", slug=recipe.slug)
    else:
        form = RecipeForm()
    return render(request, "juice_app/book_edit.html", {"form": form})


def recipe_list(request):
    """
    Displays a paginated list of recipes based on search query or category filter.
    """
    query = request.GET.get("q")
    category_id = request.GET.get("category")

    if query:
        recipes = Recipe.objects.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(ingredients__icontains=query)
            | Q(instructions__icontains=query)
        )
    elif category_id:
        recipes = Recipe.objects.filter(category_id=category_id).order_by("id")
    else:
        recipes = Recipe.objects.all().order_by("id")

    paginator = Paginator(recipes, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()

    return render(
        request,
        "juice_app/recipe_list.html",
        {
            "page_obj": page_obj,
            "recipe_list": recipes,
            "categories": categories,
            "DEBUG": DEBUG,
        },
    )


def recipe_detail(request, slug):
    """
    Displays detailed information about a recipe and handles comment submissions.
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.approved = True
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Comment submitted and awaiting approval"
            )
            return HttpResponseRedirect(reverse("recipe_detail", args=[slug]))
    else:
        comment_form = CommentForm()

    return render(
        request,
        "juice_app/recipe_detail.html",
        context={
            "recipe": recipe,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


@login_required
def comment_edit(request, slug, comment_id):
    """
    Handles editing a comment.
    Only allows editing if the comment belongs to the current user.
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment_form.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
            return HttpResponseRedirect(reverse("recipe_detail", args=[slug]))
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")
    else:
        comment_form = CommentForm(instance=comment)

    return render(
        request, "juice_app/edit_comment.html", {"comment_form": comment_form}
    )


@login_required
def comment_delete(request, slug, comment_id):
    """
    Handles deleting a comment.
    Only allows deletion if the comment belongs to the current user.
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("recipe_detail", args=[slug]))
