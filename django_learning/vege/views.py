from django.shortcuts import render, redirect
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
    queryset = Recipe.objects.all()
    context = {
        "recipes": queryset
    }
    return render(request, "recipes.html", context)

def delete_recipe(request, recipe_id):
    queryset = Recipe.objects.get(id=recipe_id)
    queryset.delete()
    return redirect('recipes')