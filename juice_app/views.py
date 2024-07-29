from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Recipe, Comment, Category
from .forms import CommentForm, RecipeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


class HomePage(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "juice_app/index.html"


@login_required
def add_juice(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm()
    return render(request, "juice_app/add_juice.html", {"form": form})


def recipe_list(request):
    category_id = request.GET.get("category", None)
    if category_id:
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
        {"page_obj": page_obj, "recipe_list": recipes, "categories": categories},
    )


@login_required
def recipe_edit(request, recipe_id):

    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == "POST":
        recipe_form = RecipeForm(
            data=request.POST, files=request.FILES, instance=recipe
        )
        if recipe_form.is_valid() and recipe.author == request.user:
            recipe_form.save()
            messages.add_message(request, messages.SUCCESS, "Recipe Updated!")
            return redirect("recipe_list")
        else:
            messages.add_message(request, messages.ERROR, "Error updating recipe!")
    else:
        recipe_form = RecipeForm(instance=recipe)

    return render(request, "juice_app/edit_recipe.html", {"recipe_form": recipe_form})


@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.author == request.user:
        recipe.delete()
        messages.add_message(request, messages.SUCCESS, "Recipe deleted successfully!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own recipes."
        )
    return redirect("recipe_list")


def recipe_detail(request, slug):
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


# ==========================================================================================================


@login_required
def comment_edit(request, slug, comment_id):
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
