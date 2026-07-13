from django.shortcuts import render, redirect,get_object_or_404
from .models import Recipe
from django.http import HttpResponse


def recipes(request):

    if request.method == "POST":
        recipe_name = request.POST.get("recipe_name")
        recipe_description = request.POST.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image
        )

        return redirect("recipes")

    queryset = Recipe.objects.all()

    if request.GET.get("search"):
        queryset = queryset.filter(
            recipe_name__icontains=request.GET.get("search")
        )

    context = {
        "recipes": queryset
    }

    return render(request, "recipes.html", context)

def delete_recipe(request, recipe_id):
    queryset = Recipe.objects.get(id=recipe_id)
    queryset.delete()
    return redirect('recipes')


def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == "POST":
        recipe.recipe_name = request.POST.get("recipe_name")
        recipe.recipe_description = request.POST.get("recipe_description")

        image = request.FILES.get("recipe_image")

        if image:
            recipe.recipe_image = image

        recipe.save()

        return redirect("recipes")

    context = {
        "recipe": recipe
    }

    return render(request, "update_recipe.html", context)