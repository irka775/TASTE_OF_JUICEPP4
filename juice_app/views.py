from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from .forms import CommentForm

class HomePage(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "juice_app/index.html"

class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "juice_app/recipe_list.html"
    paginate_by = 6

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

def comment_edit(request, slug, comment_id):
    if request.method == "POST":
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = True
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

        return HttpResponseRedirect(reverse("recipe_detail", args=[slug]))

def comment_delete(request, slug, comment_id):
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("recipe_detail", args=[slug]))
